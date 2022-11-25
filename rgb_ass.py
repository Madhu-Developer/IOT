import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
channel = [12,13,19]
for c in channel:
    GPIO.setup(c, GPIO.OUT)

# GPIO.output(channel,GPIO.LOW)
# GPIO.output(channel,GPIO.HIGH)

try:
    while True:
        try: 
            i = input("enter a number from 1 to 7 = ")
            i = int(i)
            if i < 0 or i > 7:
                print("enter the valid number ")
                continue

            rgb = format(i,'03b')
            for i,c in enumerate(channel) :
                print( i , c, rgb[i])
                GPIO.output(c ,  not bool(int(rgb[i])))    

        except ValueError as e:
            print("invalid input..,try again ")
except KeyboardInterrupt as  e:
    GPIO.cleanup()
    print("quiting...")

    
    