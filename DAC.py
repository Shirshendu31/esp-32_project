from machine import Pin, DAC import time
from time import sleep
d= DAC(Pin(26, Pin.OUT), bits=8) d.write(255)
potentiometer = ADC(Pin(35)) potentiometer.atten(ADC.ATTN_11DB)
while True:
potentiometer_value = potentiometer.read()* 3.3/4095 print(potentiometer_value)
sleep(2)
