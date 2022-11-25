import RPi.GPIO as GPIO
from time import sleep
channel = 19 
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.OUT)

p = GPIO.PWM(channel, 60)
p.start(50)

try:
    while 1:
        for dc in range(0,101,1):
            p.ChangeDutyCycle(dc)
            sleep(0.01)
        for dc in range(100,-1,-1):
            p.ChangeDutyCycle(dc)
            sleep(0.01)
except KeyboardInterrupt:
    pass

p.stop()
GPIO.Cleanup()