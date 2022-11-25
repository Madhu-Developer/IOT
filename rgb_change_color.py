import RPi.GPIO as GPIO
import time 

class RGBA():
    def __init__(self,r,g,b):
        GPIO.setmode(GPIO.BCM)
        channel =[r,g,b]
        for c in channel:
            GPIO.setup(c,GPIO.OUT)
        self.r = GPIO.PWM(r, 1000)
        self.g = GPIO.PWM(g, 1000)
        self.b = GPIO.PWM(b, 1000)
        self.r.start(0)
        self.g.start(0)
        self.b.start(0)
    
    def setcolor(self,r,g,b):
        try:
            while True:
               for r in range(1,255,1):
                    print(r,g,b)
                    r=100-(int(r)/255)*100
                    self.r.ChangeDutyCycle(r)
                    time.sleep(0.01)

               for r in range(255,-1,-1):
                    print(r,g,b)
                    r=100-(int(r)/255)*100
                    self.r.ChangeDutyCycle(r)
                    time.sleep(0.01)    
                
               for g in range(255,-1,-1):
                    print(r,g,b)
                    g=100-(int(g)/255)*100
                    self.g.ChangeDutyCycle(g)
                    time.sleep(0.01)
                
               for g in range(1,255,1):
                    print(r,g,b)
                    g=100-(int(g)/255)*100
                    self.g.ChangeDutyCycle(g)
                    time.sleep(0.01)

               for b in range(255,-1,-1):
                    print(r,g,b)
                    b=100-(int(b)/255)*100
                    self.b.ChangeDutyCycle(b)
                    time.sleep(0.01)
                
               for b in range(1,255,1):
                    print(r,g,b)
                    b=100-(int(b)/255)*100
                    self.b.ChangeDutyCycle(b)
                    time.sleep(0.01)

                                                   
        except KeyboardInterrupt:
            print("quiting...")
led = RGBA(12,13,19)
led.setcolor(0,0,0)
time.sleep(0.1)
GPIO.cleanup()
