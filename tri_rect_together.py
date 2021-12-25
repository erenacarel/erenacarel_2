from SHTC import SHTC3
from LSMDSO import LSM6DSO
import machine, time, neopixel

from time import sleep
from ili9341 import Display, color565
from machine import Pin, SPI, I2C
import utime
from gfx_triangle_lib import GFX

#np = neopixel.NeoPixel(machine.Pin(5), 4)
np = neopixel.NeoPixel(Pin(5), 4)

i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=100000)
spi = SPI(1, baudrate=40000000, sck=Pin(14), mosi=Pin(13))
display = Display(spi, dc=Pin(4), cs=Pin(16), rst=Pin(17), pixel=None)
#i2c = machine.I2C(0,scl=machine.Pin(22), sda=machine.Pin(21), freq=100000)
time.sleep(1)
print(i2c.scan())

shtc_sensor = SHTC3(i2c)
time.sleep(1)
lsm6dso = LSM6DSO(i2c)

print("SHTC3 device id:", shtc_sensor.begin())
print("LSM:", lsm6dso.begin())
lsm6dso.begin()
#b.normalizeValue()
time.sleep(0.20)
a = lsm6dso.readAccelValueXYZ()

print(a[0])
print("X, Y, Z location: ",lsm6dso.readAccelValueXYZ())

#while True:
if(a[0]>0):
    print("clockwise")
else:
    print("counter clockwise")

time.sleep(0.5)

def fast_hline(x, y, width, color):
    display.fill_rectangle(x, y, width, 1, color)

def fast_vline(x, y, height, color):
    display.fill_rectangle(x, y, 1, height, color)

graphics = GFX(240, 320, display.draw_pixel, hline=fast_hline, vline=fast_vline)

def test():
    oldPosition = 0
    position = 0
    while True:     
        x, y, z = lsm6dso.readAccelValueXYZ()
        print("X, Y, Z location: ", lsm6dso.readAccelValueXYZ())
        d1_const = (y-x)/80.0
        print("d1_const", d1_const)
        if d1_const > 1:
            d1_const = 1
        elif d1_const < 0:
            d1_const = 0
                
        d2_const = (-y-x)/80.0
        print("d2_const", d2_const)
        if d2_const > 1:
            d2_const = 1
        elif d2_const < 0:
            d2_const = 0
            
        d3_const = (x-y)/80.0
        print("d3_const", d3_const)
        if d3_const > 1:
            d3_const = 1
        elif d3_const < 0:
            d3_const = 0
            
        d4_const = (x+y)/80.0
        print("d4_const", d4_const)
        if d4_const > 1:
            d4_const = 1
        elif d4_const < 0:
            d4_const = 0
            
        d1 = int(100 * d1_const)
        d2 = int(100 * d2_const)
        d3 = int(100 * d3_const)
        d4 = int(100 * d4_const)
            
        d5 = int(200 * d1_const)
        d6 = int(200 * d2_const)
        d7 = int(200 * d3_const)
        d8 = int(200 * d4_const)
        
        np[0] = (d1,d1,d1) 
        np[1] = (d2,d2,d2)
        np[2] = (d3,d3,d3)
        np[3] = (d4,d4,d4)
        np.write()
        time.sleep(0.1)
        
        print("d5, d6, d7, d8 -> ",d5,d6,d7,d8)
        #print(d1,d2,d3,d4)
        
        if (((d5 and d6) == 0) and ((d7 and d8) != 0)):
            position = 0
                
        if (((d7 and d8) == 0) and ((d5 and d6) != 0)):
            position = 1
        
        if (((d6 and d7) == 0) and ((d5 and d8) != 0)):
            position = 2
            
        if (((d5 and d8) == 0) and ((d6 and d7) != 0)):
            position = 3
            
                    
#         if (((d5 and d6 and d7 and d8) == 0) or ((d5 and d6 and d7) == 0) or ((d6 and d7 and d8) == 0) or ((d5 and d7 and d8) == 0) or ((d5 and d6 and d8) == 0)):
#             display.clear()
#             continue
                        
        if (oldPosition != position):
            oldPosition = position
            display.clear()
            
            if position == 0: # ekranın sağ altı
                graphics.fill_triangle(239, 317, 120, 317, 239, 190, color565(0, 0, 255))
                display.fill_hrect(190, 0, 50, 320, color565(0, 0, 255))
                graphics.fill_triangle(239, 0, 239, 120, 120, 0, color565(0, 0, 255))
                                      
            elif position == 1: # ekranın sol altı
                graphics.fill_triangle(0, 120, 120, 0, 0, 0, color565(0, 0, 255))           
                display.fill_hrect(0, 0, 50, 320, color565(0, 0, 255))
                graphics.fill_triangle(120, 317, 0, 317, 0, 190, color565(0, 0, 255))
                
            elif position == 2: # ekranın en aşağısı
                graphics.fill_triangle(239, 0, 239, 120, 120, 0, color565(0, 0, 255))
                display.fill_hrect(0, 0, 240, 50, color565(0, 0, 255))
                graphics.fill_triangle(0, 120, 120, 0, 0, 0, color565(0, 0, 255))
                
            elif position == 3: # ekranın yukarısı pinli kısım
                graphics.fill_triangle(120, 317, 0, 317, 0, 190, color565(0, 0, 255))
                display.fill_hrect(0, 266, 240, 50, color565(0, 0, 255))       
                graphics.fill_triangle(239, 317, 120, 317, 239, 190, color565(0, 0, 255))
                   
test()












