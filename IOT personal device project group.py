import time
from time import sleep
from time import strftime
from time import localtime
# Servo Motor 
import RPi.GPIO as GPIO #import RPi.GPIO module
from time import sleep
 # DC Motor On & Off
import RPi.GPIO as GPIO #import RPi.GPIO module
from time import sleep
# Push Button, LED Lights & Buzzer

import RPi.GPIO as GPIO #Imports RPi’s GPIO module and call that GPIO.
from time import sleep 

GPIO.setup(19, GPIO.IN) # Make GPIO 19 an input pin. (push button)
GPIO.setmode(GPIO.BCM) #choose BCM mode
GPIO.setwarnings(False)
GPIO.setup(26,GPIO.OUT) #set GPIO 26 as output
PWM=GPIO.PWM(26,50) #set 50Hz PWM output at GPIO26
PIO.setmode(GPIO.BCM) #choose BCM mode
GPIO.setwarnings(False)
GPIO.setup(23,GPIO.OUT) #set GPIO 23 as output
GPIO.setmode(GPIO.BCM) # Pin 13 is also GPIO 27. This line says refer to the pins using their GPIO numbers. # Broadcom Mode since we are using the Broadcom chipset
GPIO.setwarnings(False) # To get rid of warning, if the GPIO pins you are using have been used before.

GPIO.setup(17, GPIO.OUT) # Make GPIO 17 an output pin. (buzzer)
GPIO.setup(19, GPIO.IN) # Make GPIO 19 an input pin. (push button)
PWM = GPIO.PWM(23,100) #set 100Hz PWM output at GPIO 23

while(True):
    # Collect Data as soon as Raspberry Pi is run
    current_time = localtime()
    alarm = "14:16:00"
    current_time = strftime("%H:%M:%S")
    print("Current Time =", current_time)
    
    # add keypad demo when number 1 is pressed, start the morning program 
    if (current_time == alarm): # when PUSH BUTTON is Pressed, or when the current time is the same as the alarm
        print("GOOD MORNING! IT'S TIME TO GET UP!")
    
    # buzzer beeps until the button is pressed

    # servo
    PWM.start(3) #3% duty cycle
    print('duty cycle:', 3) #3 o'clock position
    sleep(4) #allow time for movement
    PWM.start(13) #13% duty cycle
    print('duty cycle:', 13) #9 o'clock position
    sleep(4) #allow time for movement

    # DC Motor
    GPIO.output(23,1) #output logic high/'1'
    sleep(1) #delay 1 second
    GPIO.output(23,0) #output logic low/'0'
    sleep(1) #delay 1 second
    
    #DC Motor Speed Control
    for i in range(0,101,25):
        PWM.start(i)
        sleep(0.5)

    for x in range(10):
        GPIO.output(17,1) # Buzzer turns on
        sleep(0.5)
        GPIO.output(17,0) # Buzzer turns off
        sleep(0.5)
    


    


