import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
channel = 27

GPIO.setup(channel, GPIO.IN)

while True:
    # if(GPIO.input(channel) == GPIO.HIGH):
    #     print("Button Pressed ")
    #     time.sleep(0.1)
    if(GPIO.wait_for_edge(channel,GPIO.RISING ,timeout=1000)):
        print("button is pressed")
        print("button pressed at "+str(time.time()))
        
    if(GPIO.wait_for_edge(channel,GPIO.FALLING , timeout ==1000 )):
        print("button is not pressed")
        print("button off at "+str(time.time()))
