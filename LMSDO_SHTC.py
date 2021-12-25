######## LSMDSO Library ########
import time
import machine

LSM6DSO_ADDRESS = 106

WHO_AM_I_REGISTER = 0x0F
WHO_AM_I_VALUE = 0x6C

XL_VALUE_LENGTH = 6
XL_SENSITIVITY =  .061 * 1e-3 * 9.81 # mg/LSB
XL_SCALE = 8

class LSM6DSO:

    def __init__(self,i2c, i2c_address=LSM6DSO_ADDRESS, acc_sens=XL_SENSITIVITY, acc_scale=XL_SCALE):
        self.i2c = i2c
        self.i2c_address = i2c_address
        self.acc_sens = acc_sens
        self.acc_scale = acc_scale


    def begin(self):
        self.i2c.writeto(self.i2c_address, bytearray([WHO_AM_I_REGISTER]))
        who_am_i = self.i2c.readfrom(self.i2c_address, 1)[0]
        if who_am_i != WHO_AM_I_VALUE:
            return False

        self.i2c.writeto_mem(self.i2c_address,0x11,bytearray([0x4c]))
        self.i2c.writeto_mem(self.i2c_address,0x10,bytearray([0x4a]))
        self.i2c.writeto_mem(self.i2c_address,0x16,bytearray([0x00]))
        self.i2c.writeto_mem(self.i2c_address,0x17,bytearray([0x09]))

        return True

    def normalizeValue(self, raw_value):
        mask = 2**(15)
        twos_complement = -(raw_value & mask) + (raw_value & ~mask)
        return twos_complement*self.acc_sens*self.acc_scale

    def readAccelValueXYZ(self):
        self.i2c.writeto(self.i2c_address,bytearray([0x28]))
        data = self.i2c.readfrom(self.i2c_address,XL_VALUE_LENGTH)
        x = (data[1] << 8) | data[0]
        x = self.normalizeValue(x)
        
        y = (data[3] << 8) | data[2]
        y = self.normalizeValue(y)

        z =  (data[5] << 8) | data[4]
        z = self.normalizeValue(z)

        return x,y,z
        
############ SHTC Library ###########
SHTC_ADDRESS = 0x70
SHTC_CMD_WAKE = bytearray([0x35,0x17])
SHTC_CMD_READ_ID = bytearray([0xEF,0xC8])
SHTC_CMD_CSE_TF_NPM  = bytearray([0x7C, 0xA2])
SHTC_PAYLOAD_LENGTH = 6

SHTC_NO_ERROR = 0
SHTC_CS_ERROR = 1


class SHTC3:
    def __init__(self, i2c_dev, delay_function=time.sleep_ms):
        self.i2c_dev = i2c_dev
        self.error_state = SHTC_NO_ERROR
        self.device_id = 0
        self.delay_= delay_function
        
    def begin(self):        # returns device id
        self.i2c_dev.writeto(SHTC_ADDRESS, SHTC_CMD_WAKE)
        self.delay_(500)
        self.i2c_dev.writeto(SHTC_ADDRESS, SHTC_CMD_READ_ID)
        id_buffer = self.i2c_dev.readfrom(SHTC_ADDRESS, 2)
        self.device_id = (id_buffer[0] << 8) | id_buffer[1]
        self.i2c_dev.writeto(SHTC_ADDRESS, SHTC_CMD_CSE_TF_NPM)
        return self.device_id
        
    def verifyChecksum(self, raw_values, rcv_cs):
        cs = 0xFF
        poly = 0x31
        for i in range(2):
            cs ^= raw_values[i]
            for c in range(8):
                if (cs & 0x80):
                    cs = ((cs<<1) ^ poly) & 0xFF
                else:
                    cs <<= 1
            
        if rcv_cs == cs:
            return True
        else :
            return False
    
    def readRawValues(self):
        self.i2c_dev.writeto(SHTC_ADDRESS, SHTC_CMD_CSE_TF_NPM)
        self.delay_(20)                   # required by the sensor
        i2c_buffer = self.i2c_dev.readfrom(SHTC_ADDRESS, SHTC_PAYLOAD_LENGTH)
        isTempVerified = self.verifyChecksum([i2c_buffer[0], i2c_buffer[1]], i2c_buffer[2])              # verifying temperature data checksum
        isHumidityVerified =  self.verifyChecksum([i2c_buffer[3], i2c_buffer[4]], i2c_buffer[5])         # verifying humidity data checksum
        
        if (isHumidityVerified and isTempVerified) == False:
            self.error_state = SHTC_CS_ERROR
            
        raw_temp = (i2c_buffer[1] | (i2c_buffer[0] << 8))
        raw_humidity = (i2c_buffer[4] | (i2c_buffer[3] << 8))
        
        return raw_temp, raw_humidity

    def readValues(self, fahrenheit=False):
        raw_temp, raw_humidity = self.readRawValues()
        temp = -45.0 + (raw_temp * 175 / 65536.0)       # temperature in celcius
        if fahrenheit:
            temp = temp * (9.0 / 5) + 32.0              # temperature in fahrenheit
        humidity = raw_humidity * 100 / 65536.0         # humidity value per cent 
        return temp, humidity
    
    
    
   
    
    
    
    
    
    
    
    
    
    
    

