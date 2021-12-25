## Değerler beraber yazıyor
## Konuma göre ledler yanacak
from ili9341 import Display,color565
from machine import I2C, Pin, SPI
import time
from LMSDO_SHTC3 import LSM6DSO, SHTC3
from neopix import WS2812
from xglcd_font import XglcdFont
from gfx_triangle_lib import GFX
from random import randint
import neopixel
from LDR import LDR, BUTTON


np = neopixel.NeoPixel(Pin(5), 4)
i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=100000)
spi = SPI(1, baudrate=40000000, sck=Pin(14), mosi=Pin(13))
display = Display(spi, dc=Pin(4), cs=Pin(16), rst=Pin(17), pixel=None)

time.sleep(1)

tempSensor = SHTC3(i2c)
time.sleep(1)
lsm = LSM6DSO(i2c)
neoLed = WS2812()
button1 = BUTTON(1, 25, Pin.IN) #15

lsm.begin()
time.sleep(0.1)
tempSensor.begin()
time.sleep(0.1)

print("X, Y, Z location: ", lsm.readAccelValueXYZ())
print("Tempratue and Humidity: ", tempSensor.readValues())

def fast_hline(x, y, width, color):
    display.fill_rectangle(x, y, width, 1, color)

def fast_vline(x, y, height, color):
    display.fill_rectangle(x, y, 1, height, color)

graphics = GFX(240, 320, display.draw_pixel, hline=fast_hline, vline=fast_vline)

def test():
    oldPosition = 0
    position = 0
    print('Loading fonts...')
    print('Loading espresso_dolce')
    espresso_dolce = XglcdFont('EspressoDolce18x24.c', 18, 24)
    while True:
        accelValues = lsm.readAccelValueXYZ()
        tempHumValues = tempSensor.readValues()
        but_val = button1.value()
        display.draw_text(60, 10, 'X:   %f' %accelValues[0],  espresso_dolce, color565(0, 255, 255))
        display.draw_text(60, 40, 'Y:   %f' %accelValues[1], espresso_dolce, color565(0, 255, 255))
        display.draw_text(60, 70, 'Z:   %f' %accelValues[2], espresso_dolce, color565(0, 255, 255))
        graphics.line(0, 100, 237, 100, color565(255, 0, 0))
        display.draw_text(5, 110, 'Sicaklik:  %f' %tempHumValues[0] ,espresso_dolce, color565(0, 255, 255))
        display.draw_text(5, 140, 'Nem:  %f' %tempHumValues[1] ,espresso_dolce, color565(0, 255, 255))
        graphics.line(0, 170, 237, 170, color565(255, 0, 0))
        display.draw_text(5, 180, 'Button:  %d' %but_val, espresso_dolce, color565(0, 255, 255))
        
        x,y,z = lsm.readAccelValueXYZ()
        #print("X, Y, Z location: ", lsm6dso.readAccelValueXYZ())
        d1_const = (y-x)/80.0
        #print("d1_const", d1_const)
        if d1_const > 1:
            d1_const = 1
        elif d1_const < 0:
            d1_const = 0
                
        d2_const = (-y-x)/80.0
        #print("d2_const", d2_const)
        if d2_const > 1:
            d2_const = 1
        elif d2_const < 0:
            d2_const = 0
            
        d3_const = (x-y)/80.0
        #print("d3_const", d3_const)
        if d3_const > 1:
            d3_const = 1
        elif d3_const < 0:
            d3_const = 0
            
        d4_const = (x+y)/80.0
        #print("d4_const", d4_const)
        if d4_const > 1:
            d4_const = 1
        elif d4_const < 0:
            d4_const = 0
            
        d5 = int(200 * d1_const)
        d6 = int(200 * d2_const)
        d7 = int(200 * d3_const)
        d8 = int(200 * d4_const)
        
        #print(d5,d6,d7,d8)
        
        if (((d5 and d6) == 0) and ((d7 and d8) != 0)):
            position = 0
                
        if (((d7 and d8) == 0) and ((d5 and d6) != 0)):
            position = 1
                
        if (((d6 and d7) == 0) and ((d5 and d8) != 0)):
            position = 2
            
        if (((d5 and d8) == 0) and ((d6 and d7) != 0)):
            position = 3
            
        if ((d6<10) and (10<d7<140) and (d8<10)):
            position = 4
            
        if ((d7<35) and (10<d8<140) and (d5<10)):
            position = 5
            
        if ((10<d5<140) and (d6<10) and (d8<10)):
            position = 6
            
        if ((d5<10) and (10<d6<140) and (d7<35)):
            position = 7
 
        if (oldPosition != position):
            oldPosition = position
            #display.clear()
            
            if position == 0: # ekranın sağ altı
                np[0] = (0,0,0)
                np[1] = (0,0,0)
                np[3] = (randint(0, 255), randint(0, 255), randint(0, 255))
                np[2] = (randint(0, 255), randint(0, 255), randint(0, 255))
                np.write()
                #time.sleep(0.1)
                
            elif position == 1: # ekranın sol altı
                np[0] = (randint(0, 255), randint(0, 255), randint(0, 255))
                np[1] = (randint(0, 255), randint(0, 255), randint(0, 255))
                np[2] = (0,0,0)
                np[3] = (0,0,0)
                np.write()
                #time.sleep(0.1)
                
            elif position == 3: # ekranın en aşağısı
                np[0] = (0,0,0)
                np[1] = (randint(0, 255), randint(0, 255), randint(0, 255))
                np[2] = (randint(0, 255), randint(0, 255), randint(0, 255))
                np[3] = (0,0,0)
                np.write()
                #time.sleep(0.1)
                
            elif position == 2: # ekranın yukarısı pinli kısım
                np[0] = (randint(0, 255), randint(0, 255), randint(0, 255))
                np[1] = (0,0,0)
                np[2] = (0,0,0)
                np[3] = (randint(0, 255), randint(0, 255), randint(0, 255))
                np.write()
                #time.sleep(0.1)
                
            elif position == 4: # sağ alt çapraz
                np[0] = (0,0,0)
                np[1] = (0,0,0)
                np[2] = (randint(0, 255), randint(0, 255), randint(0, 255))
                np[3] = (0,0,0)
                np.write()
                #time.sleep(0.1)
                
            elif position == 5: # sağ üst çapraz
                np[0] = (0,0,0)
                np[1] = (0,0,0)
                np[2] = (0,0,0)
                np[3] = (randint(0, 255), randint(0, 255), randint(0, 255))
                np.write()
                #time.sleep(0.1)
                
            elif position == 6: # sol üst çapraz
                np[0] = (randint(0, 255), randint(0, 255), randint(0, 255))
                np[1] = (0,0,0)
                np[2] = (0,0,0)
                np[3] = (0,0,0)
                np.write()
                #time.sleep(0.1)
                
            elif position == 7: # sol alt çapraz
                np[0] = (0,0,0)
                np[1] = (randint(0, 255), randint(0, 255), randint(0, 255))
                np[2] = (0,0,0)
                np[3] = (0,0,0)
                np.write()
                #time.sleep(0.1)
                
test()


