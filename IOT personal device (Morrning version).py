import I2C_LCD_driver
from time import *
from time import sleep
from datetime import datetime

# Servo Motor 
import RPi.GPIO as GPIO #import RPi.GPIO module
from time import sleep
 # DC Motor On & Off
import RPi.GPIO as GPIO #import RPi.GPIO module
from time import sleep
# Push Button, LED Lights & Buzzer

import RPi.GPIO as GPIO #Imports RPi’s GPIO module and call that GPIO.
from time import sleep 

GPIO.setmode(GPIO.BCM) #choose BCM mode
GPIO.setup(19, GPIO.IN) # Make GPIO 19 an input pin. (push button)
GPIO.setwarnings(False)
GPIO.setup(26,GPIO.OUT) #set GPIO 26 as output
PWM_servo =GPIO.PWM(26,50) #set 50Hz PWM output at GPIO26
GPIO.setwarnings(False)
GPIO.setup(24,GPIO.OUT) #set GPIO 23 as output (LED)
GPIO.setup(23,GPIO.OUT) #set GPIO 23 as output (DC Motor)
GPIO.setwarnings(False) # To get rid of warning, if the GPIO pins you are using have been used before.
GPIO.setup(18, GPIO.OUT) # Make GPIO 18 an output pin. (buzzer)
PWM_dc = GPIO.PWM(23,100) #set 100Hz PWM output at GPIO 23
"""
The green LED should light up for 15 sec, followed by
the yellow LED for 2 sec, followed by the red LED for 10
sec. The buzzer should beep (on and off) at 1 sec
interval when the red LED is lighting up ( we don’t
have a “green man” which should light up when the red
LED is lighting up). Pressing the button will cause the
green LED’s time to be reduced to 10 sec.

"""

LCD = I2C_LCD_driver.lcd() #instantiate an lcd object, call it LCD
sleep(0.5)
LCD.backlight(0) #turn backlight off
sleep(0.5)


LCD.backlight(1) #turn backlight on 
LCD.lcd_display_string("LCD Display Test", 1) #write on line 1
LCD.lcd_display_string(str(datetime.now().time()), 2, 2) #write on line 2
              #starting on 3rd column

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


    PWM_servo.start(3) #3% duty cycle
    print('duty cycle:', 3) #3 o'clock position
    sleep(4) #allow time for movement
    PWM_servo.start(13) #13% duty cycle
    print('duty cycle:', 13) #9 o'clock position
    sleep(4) #allow time for movement

    #LED
    GPIO.output(24,1) #output logic high/'1'
    sleep(1) #delay 1 second
    GPIO.output(24,0) #output logic low/'0'
    sleep(1) #delay 1 second
 #DC Motor Speed Control
    

  
    for i in range(0,101,25):
        PWM_dc.start(i)
        sleep(0.5)
    PWM_dc.start(0)
    for x in range(10):
        GPIO.output(18,1) # Buzzer turns on
        sleep(0.5)
        GPIO.output(18,0) # Buzzer turns off
        sleep(0.5)
    


    


