from machine import Pin import time
from time import sleep
led = Pin(32, Pin.OUT)
while true: led.value(1)
time.sleep(0.5) led.value(0) time.sleep(0.5)
 
