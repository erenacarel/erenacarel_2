### neopixel kütüphanesi
from machine import Pin
import neopixel
import time
from random import randint

class WS2812():
    def __init__(self, pin_number=5, num_pixels=4):
        self.num_pixels = num_pixels
        self.pixels = neopixel.NeoPixel(Pin(pin_number), num_pixels)
        self.np = neopixel.NeoPixel(Pin(pin_number),num_pixels) 
    
#     def __init__(self, pin_number=5, num_pixels=4):
#         self.num_pixels = num_pixels
#         self.np = neopixel.NeoPixel(Pin(pin_number),num_pixels)
    
    def ErasePixels(self):
        for i in range(self.num_pixels):
            self.np[i] = (0,0,0)
            self.np.write()
            time.sleep(.1)
            
    def random_fill(self): 
        for i in range(0, self.num_pixels, 1):
            self.pixels[i] = (randint(0,255), randint(0,255), randint(0,255))
            self.np.write()
            time.sleep(.1)
        
        for i in range(self.num_pixels, 0, -1):
            self.np[i-1] = (randint(0,255), randint(0,255), randint(0,255))
            self.np.write()
            time.sleep(.1)
        
    def fill(self, color):
        for pixel in range(self.num_pixels):
            self.np[pixel] = color
        self.np.write() 

# c = WS2812()          
# while True:
#     c.random_fill()
#     c.ErasePixels()
#     b.begin()
#     #b.normalizeValue()
#     time.sleep(0.20)
#     print("X, Y, Z location: ",b.readAccelValueXYZ())