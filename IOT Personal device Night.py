import Adafruit_DHT

import RPi.GPIO as GPIO
import sys
from mfrc522 import SimpleMFRC522
# IR (PIR) Sensor
import RPi.GPIO as GPIO #import RPi.GPIO module
from time import sleep
# LCD Display (Line)
import I2C_LCD_driver #import the library

GPIO.setwarnings(False)
reader = SimpleMFRC522()
auth = []
GPIO.setmode(GPIO.BCM) #choose BCM mode
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.IN) # set GPIO 17 as input
LCD = I2C_LCD_driver.lcd() #instantiate an lcd object, call it LCD
sleep(0.5)
LCD.backlight(0) #turn backlight off
sleep(0.5)
LCD.backlight(1) #turn backlight on
LCD.lcd_display_string("LCD Display Test", 1) #write on line 1
LCD.lcd_display_string("Address = 0x27", 2, 2) #write on line 2


sleep(5) #to allow sensor time to stabilize
PIR_state=0 #use this, so that only a change in state is reported


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

        
if GPIO.input(17): #read a HIGH i.e. motion is detected
        if PIR_state==0:
            print('detected HIGH i.e. motion detected')
            PIR_state=1
        else: #read a LOW i.e. no motion is detected
            if PIR_state==1:
                print('detected LOW i.e. no motion detected')
                PIR_state=0
        sleep(1)


        print('…')
#starting on 3rd column
sleep(2) #wait 2 sec
LCD.lcd_clear() #clear the display








        
