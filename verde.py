
import RPi.GPIO as gpio
import time

buzzer=14
ledVerde=20
ledRojo=21

gpio.setmode(gpio.BCM)
gpio.setup(ledVerde, gpio.OUT)
gpio.setup(buzzer, gpio.OUT)
gpio.setup(ledRojo, gpio.OUT)
gpio.output(ledRojo, False)
gpio.output(ledVerde, True)
gpio.output(buzzer, True)
time.sleep(0.5)
gpio.output(ledVerde, False)
gpio.output(buzzer, False)
time.sleep(0.5)
gpio.output(ledVerde, True)
gpio.output(buzzer, True)
time.sleep(0.5)
gpio.output(ledVerde, False)
gpio.output(buzzer, False)
time.sleep(0.5)
gpio.output(ledVerde, True)
gpio.output(buzzer, True)
time.sleep(0.5)
gpio.output(ledVerde, False)
gpio.output(buzzer, False)


