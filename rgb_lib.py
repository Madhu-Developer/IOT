
import RPi.GPIO as GPIO
import time 
from colour import Color

class RGBA():
    def __init__(self,r,g,b):
        GPIO.setmode(GPIO.BCM)
        channel =[r,g,b]
        for c in channel:
            GPIO.setup(c,GPIO.OUT)
        self.r = GPIO.PWM(r, 60)
        self.g = GPIO.PWM(g, 100)
        self.b = GPIO.PWM(b, 100)
        self.r.start(0)
        self.g.start(0)
        self.b.start(0)


    def setrgb(self,rgb):
        r=abs(rgb[0]*100-100)
        g=abs(rgb[1]*100-100)
        b=abs(rgb[2]*100-100)    
        self.r.ChangeDutyCycle(int(r))
        self.g.ChangeDutyCycle(int(g))
        self.b.ChangeDutyCycle(int(b))

led = RGBA(12,13,19)
led.setrgb(colour("red").rgb)
time.sleep(1)
GPIO.cleanup()


