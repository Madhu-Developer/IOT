import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
channel = 19 
GPIO.setup(channel, GPIO.OUT)

while True:
    print("turning on LED...")
    GPIO.output(channel,GPIO.HIGH)
    sleep(1)
    print("turning off LED...")
    GPIO.output(channel,GPIO.LOW)
    sleep(1)
    