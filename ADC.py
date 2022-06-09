from machine import Pin, ADC import time
from time import sleep
led = Pin(32, Pin.OUT)
led.value(1)
potentiometer = ADC(Pin(35)) potentiometer.atten(ADC.ATTN_11DB)
while True:
potentiometer_value = potentiometer.read() print(potentiometer_value)
sleep(2)
