import time
import RPi.GPIO as GPIO
from threading import Thread
from colour import Color 

GPIO.setmode(GPIO.BCM)
button=27
GPIO.setup(button, GPIO.IN)
speed = 0.1
stop = False

class rgba():

    def __init__(self,r,g,b):
        GPIO.setmode(GPIO.BCM)
        channel =[r,g,b]
        for c in channel :
            GPIO.setup(c,GPIO.OUT)
        self.r = GPIO.PWM(r, 120)
        self.g = GPIO.PWM(g, 120)
        self.b = GPIO.PWM(b, 120)
        self.r.start(0)
        self.g.start(0)
        self.b.start(0)
    
    def setrgb(self, rgb):
        r = abs(rgb[0] * 100 - 100)
        g = abs(rgb[1] * 100 - 100)
        b = abs(rgb[2] * 100 - 100)
        # print(r, g, b)
        self.r.ChangeDutyCycle(int(r))
        self.g.ChangeDutyCycle(int(g))
        self.b.ChangeDutyCycle(int(b))

def rgb_transition_thread():
    led = rgba(12,13,19)
    while True:
        if stop :
            break 
        for i in Color("red").range_to(Color("orange"),100):
            led.setrgb(i.rgb)
            time.sleep(speed)
        for i in Color("orange").range_to(Color("yellow"),100):
            led.setrgb(i.rgb)
            time.sleep(speed)
            
        for i in Color("yellow").range_to(Color("green"),100):
            led.setrgb(i.rgb)
            time.sleep(speed)
            
        for i in Color("green").range_to(Color("blue"),100):
            led.setrgb(i.rgb)
            time.sleep(speed)
            
        for i in Color("blue").range_to(Color("indigo"),100):
            led.setrgb(i.rgb)
            time.sleep(speed)
            
        for i in Color("indigo").range_to(Color("violet"),100):
            led.setrgb(i.rgb)
            time.sleep(speed)

t = Thread(target=rgb_transition_thread)
t.start()
stime=None 
try :
    while True:
        if(GPIO.wait_for_edge(button,GPIO.RISING ,timeout=5000)):
            #print("button pressed at "+str(time.time()))
            stime=time.time()
        
        if(GPIO.wait_for_edge(button,GPIO.FALLING , timeout =5000 )):
            #print("button off at "+str(time.time()))
            ltime=time.time() - stime
            print(speed )
            speed = ltime /10




except KeyboardInterrupt :
    stop = True 
    t.join()
    GPIO.cleanup()
    print("quiting.....")