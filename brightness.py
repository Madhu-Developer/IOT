import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
channel = 19 
GPIO.setup(channel, GPIO.OUT)

p = GPIO.PWM(channel, 100)
p.start(100)
i= None
try:
    while i != 'q': 
        try:
                d= input("Enter the brightness in which the led sholud glow : ")
                # f=input("enter the frequency ")
                if(d == 'q'):
                    break
                # p.ChangeFrequency(int(f))  
                p.ChangeDutyCycle(int(d))
        except Exception as e:
                pass
except Exception as e:
    print("pressed ctrl+c -> Quitting......")
    pass


p.stop()
GPIO.cleanup()