import Adafruit_DHT
import time
from time import sleep
from time import strftime
from time import localtime
import datetime

import RPi.GPIO as GPIO #Imports RPi’s GPIO module and call that GPIO.
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(19, GPIO.IN) # Make GPIO 19 an input pin. (push button)
GPIO.setup(17, GPIO.OUT) # Make GPIO 17 an output pin. (buzzer)

while(True):
    # Type your code here
    print("Hello World!")
    curtain = 1
    light = 0
    display = 0
    rfid = 0
    current_time = 0 # fix
    sleep_time = 0 # fix

    # RFID Detects entry
    if (rfid == 1):

        # Play Music
        # Switch on LED light
        GPIO.output(12,1)
        # Switch on Display

        # Close Curtains
        PWM.start(3) #3% duty cycle
        print('duty cycle:', 13) #9 o'clock position
        sleep(4) #allow time for movement
        PWM.start(13) #13% duty cycle
        print('duty cycle:', 3) #3 o'clock position
        sleep(4) #allow time for movement
        
    # sleep button pressed or when reached a certain timer
    elif (GPIO.input(13,1) or current_time == sleep_time):

        # stop playing music
        # Switch off LED
        GPIO.output(12,0)
        # Switch off LCD Display
