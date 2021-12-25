### LDR ve BUTTON beraberdir.
from machine import Pin,ADC
import time
from time import sleep

class LDR:
    def __init__(self, pin, min_value=0, max_value=100):
        if min_value >= max_value:
            raise Exception("Min value is greater or equal to max value")
        
        # initialize ADC
        self.adc = ADC(Pin(pin))
        
        # set 11 dB input attenuation (voltage range 0.0v - 3.6v)
        self.adc.atten(ADC.ATTN_11DB)
        
        self.min_value = min_value
        self.max_value = max_value
        
    def read(self):
        return self.adc.read()
        # return A value from 0 to 4095
    
    def value(self): # 4095 2'12 # 12 bit ADC
        return ((self.max_value - self.min_value)*self.read()/4095)
    
class BUTTON:
    def __init__(self, button_number, pin_number, pin_state):
        self.button_number = button_number
        self.push_button_1 = Pin(pin_number, pin_state)
        self.push_button_2 = Pin(pin_number, pin_state)
        
    def value(self):
        if self.button_number == 1:
            return (self.push_button_1.value())
        if self.button_number == 2:
            return (self.push_button_2.value())
            
# while True:
#     a = BUTTON(1, 25, Pin.IN)
#     b = BUTTON(2, 15, Pin.IN)
#     print(a.value())
#     print(b.value())
#     time.sleep(1) 

