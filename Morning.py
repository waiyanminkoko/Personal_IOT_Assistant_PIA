import Adafruit_DHT
import time
from time import sleep
from time import strftime
from time import localtime
import datetime


import RPi.GPIO as GPIO #Imports RPi’s GPIO module and call that GPIO.
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


GPIO.setup(26,GPIO.OUT) #set GPIO 26 as output
PWM=GPIO.PWM(26,50) #set 50Hz PWM output at GPIO26

GPIO.setup(19, GPIO.IN) # Make GPIO 19 an input pin. (push button)
GPIO.setup(17, GPIO.OUT) # Make GPIO 17 an output pin. (buzzer)

while(True):
    # Collect Data as soon as Raspberry Pi run
    current_time = localtime()
    alarm = "14:16:00:00"
    current_time = strftime("%H:%M:%S")
    print("Current Time =", current_time)
    snooze = 0
    curtain = 0
    light = 0
    display = 0
    rfid = 1

    if (rfid == 1):

        # add keypad demo when number 1 is pressed, start the morning progra
        # buzzer beeps until the button is pressed 
        if (current_time == alarm and snooze == 0): # when alarm has not been snoozed, or when the current time is the same as the alarm
            print("GOOD MORNING! IT'S TIME TO GET UP!")
            GPIO.output(17,1) # Buzzer
            if (GPIO.input(19,1)):
                GPIO.output(17,0)
                snooze += 1
        # play music
        elif ():
            print("Opening VLC Player")
        # open curtain 
        elif (curtain == 0):
            PWM.start(3) #3% duty cycle
            print('duty cycle:', 3) #3 o'clock position
            sleep(4) #allow time for movement
            PWM.start(13) #13% duty cycle
            print('duty cycle:', 13) #9 o'clock position
            sleep(4) #allow time for movement
        
        
        
        # switch on ceiling light and display
        elif (light == 0 or display == 0):
            GPIO.output(17,1)
            #Display
        
    # when RFID detects exit
    elif (rfid == 0):
        # Switch off Lights
        GPIO.output(17,0)        
    # Switch off LCD Display
    # stop music





    