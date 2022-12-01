import RPi.GPIO as GPIO
import time 

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
    
    def setcolor(self,r,g,b):
        try:
            while True:
                r=input("enter the value for r = ")
                g=input("enter the value for g = ")
                b=input("enter the value for b = ") 
                r=100-(int(r)/255)*100
                g=100-(int(g)/255)*100
                b=100-(int(b)/255)*100
                self.r.ChangeDutyCycle(r)
                self.g.ChangeDutyCycle(g)
                self.b.ChangeDutyCycle(b)
                                                   
        except KeyboardInterrupt:
            print("quiting...")
    

led = RGBA(12,13,19)
led.setcolor(255,255,0)
time.sleep(0.01)
GPIO.cleanup()