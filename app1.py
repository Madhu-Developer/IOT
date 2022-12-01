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

    def setrgb(self,rgb):
        r=abs(rgb[0]*100-100)
        g=abs(rgb[1]*100-100)
        b=abs(rgb[2]*100-100)    
        self.r.ChangeDutyCycle(int(r))
        self.g.ChangeDutyCycle(int(g))
        self.b.ChangeDutyCycle(int(b))

led = RGBA(12,13,19)
x=int(input("enter 1 for choosing your own colour or  enter 2 for auto generation = "))


if x == 1:
      led.setcolor(255,255,255)
      GPIO.cleanup()    
elif x == 2 :
    try:   
        print("loop1")
        for i in Color("red").range_to(Color("blue"),10000):
            led.setrgb(i.rgb)
            print(i.rgb)
            time.sleep(0.001)
        print("loop2")
        for a in Color("blue").range_to(Color("red"),10000):
            led.setrgb(a.rgb)
            print(a.rgb)
            time.sleep(0.001)
        print("loop3")
        for i in Color("red").range_to(Color("blue"),10000):
            led.setrgb(i.rgb)
            print(i.rgb)
            time.sleep(0.1)
        print("loop4")
        for b in Color("blue").range_to(Color("red"),10000):
            led.setrgb(b.rgb)
            print(b.rgb)
            time.sleep(0.1)
            
        GPIO.cleanup()
    except KeyboardInterrupt :
        print("quiting........")
        GPIO.cleanup()
else :
    print("pls enter the 1 or 2 Quiting...")
    GPIO.cleanup()    

