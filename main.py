## Burada Tanımlar ile onların değerleri ayrı ayrı yazılmıştır.
## Sebebi ise led ekranda daha hızlı olmaktır.
## Ledlerimiz random yanacaktır.
## Küsüratlı değerleri yok etmek için boşluk atadık, ayrıca yuvarlama(round) yaptık.

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
button2 = BUTTON(2, 15, Pin.IN) #15

lsm.begin() ## LSM6DSO başlatılmalıdır
time.sleep(0.1)
tempSensor.begin() ## SHTC3 başlatılmalıdır.
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
    graphics.line(0, 100, 237, 100, color565(255, 0, 0))
    graphics.line(0, 170, 237, 170, color565(255, 0, 0))
    display.draw_text(5, 210, 'Button2:', espresso_dolce, color565(0, 255, 255))
    display.draw_text(5, 180, 'Button1:', espresso_dolce, color565(0, 255, 255))
    display.draw_text(5, 140, 'Nem:' ,espresso_dolce, color565(0, 255, 255))
    display.draw_text(5, 110, 'Sicaklik:',espresso_dolce, color565(0, 255, 255))
    display.draw_text(40, 10, 'X:', espresso_dolce, color565(0, 255, 255))
    display.draw_text(40, 40, 'Y:', espresso_dolce, color565(0, 255, 255))
    display.draw_text(40, 70, 'Z:', espresso_dolce, color565(0, 255, 255))

    while True:
        accelValues = lsm.readAccelValueXYZ()
        tempHumValues = tempSensor.readValues()
        but_val = button1.value()
        but_val2 = button2.value()
        display.draw_text(85, 10, "          ", espresso_dolce, color565(0, 255, 255))
        display.draw_text(60, 10, str(round(accelValues[0], 3)),  espresso_dolce, color565(0, 255, 255))
        display.draw_text(85, 40, "          ", espresso_dolce, color565(0, 255, 255))
        display.draw_text(60, 40, str(round(accelValues[1], 3)), espresso_dolce, color565(0, 255, 255))
        display.draw_text(85, 70, "          ", espresso_dolce, color565(0, 255, 255))
        display.draw_text(60, 70, str(round(accelValues[2], 3)), espresso_dolce, color565(0, 255, 255))
        
        display.draw_text(90, 110, str(round(tempHumValues[0], 2)) ,espresso_dolce, color565(0, 255, 255))
        display.draw_text(80, 140, str(round(tempHumValues[1], 2)) ,espresso_dolce, color565(0, 255, 255))
        display.draw_text(85, 180,  "  ", espresso_dolce, color565(0, 255, 255))
        display.draw_text(90, 180,  str(but_val), espresso_dolce, color565(0, 255, 255))
        display.draw_text(85, 210,  "  ", espresso_dolce, color565(0, 255, 255))
        display.draw_text(90, 210,  str(but_val2), espresso_dolce, color565(0, 255, 255))

 
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
                #time.sleep(0.1),
            
        if position < 7:
            position += 1
        else:
            position = 0
                
test()

