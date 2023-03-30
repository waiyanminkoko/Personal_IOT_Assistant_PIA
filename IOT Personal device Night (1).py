import Adafruit_DHT

import RPi.GPIO as GPIO
import sys
from mfrc522 import SimpleMFRC522



from time import sleep
# LCD Display (Line)
import I2C_LCD_driver #import the library

GPIO.setmode(GPIO.BCM) #choose BCM mode, refer to pins as GPIO no.
GPIO.setwarnings(False)
GPIO.setup(24,GPIO.OUT) #set GPIO 24 as output
GPIO.setwarnings(False)
reader = SimpleMFRC522()
auth = []
GPIO.setmode(GPIO.BCM) #choose BCM mode
GPIO.setwarnings(False)
GPIO.setup(26,GPIO.OUT) #set GPIO 26 as output
PWM=GPIO.PWM(26,50) #set 50Hz PWM output at GPIO26






GPIO.output(24,1) #output logic high/'1'

LCD = I2C_LCD_driver.lcd() #instantiate an lcd object, call it LCD
sleep(0.5)
LCD.backlight(0) #turn backlight off
sleep(0.5)
LCD.backlight(1) #turn backlight on
LCD.lcd_display_string("LCD Display Test", 1) #write on line 1
LCD.lcd_display_string("Address = 0x27", 2, 2) #write on line 2



while(True):
   print("Hold card near the reader to check if it is in the database")
        id = reader.read_id()
        id = str(id)
        f = open("authlist.txt", "r+")
        if f.mode == "r+":
              auth=f.read()
        if id in auth:
              number = auth.split('\n')
              pos = number.index(id)
              print("Card with UID", id, "found in database entry #", pos, "; access granted")
        else:
              print("Card with UID", id, "not found in database; access denied")
        sleep(2)

   PWM.start(3) #3% duty cycle
    print('duty cycle:', 3) #3 o'clock position
    sleep(4) #allow time for movement
    PWM.start(13) #13% duty cycle
    print('duty cycle:', 13) #9 o'clock position
    sleep(4) #allow time for movement

   #LED
    GPIO.output(24,1) #output logic high/'1'
    sleep(1) #delay 1 second
    GPIO.output(24,0) #output logic low/'0'
    sleep(1) #delay 1 second

   
        
#starting on 3rd column
sleep(2) #wait 2 sec
LCD.lcd_clear() #clear the display








        
