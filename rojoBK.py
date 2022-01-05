import RPi.GPIO as gpio
import time
ledRojo=21
buzzer=14

gpio.setmode(gpio.BCM)
gpio.setup(ledRojo, gpio.OUT)
gpio.setup(buzzer, gpio.OUT)

for i in range(0,10):
    time.sleep(0.1)
    gpio.output(ledRojo, True)
    gpio.output(buzzer, True)
    time.sleep(0.1)
    gpio.output(ledRojo, False)
    gpio.output(buzzer, False)

