# Temperature Sensor

import Adafruit_DHT
from time import sleep

sensor = Adafruit_DHT.AM2302 # refer to AM2302 as "temperature and humidity sensor"
pin = 4 # sensor output connected to GPIO 4

while (True):
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    # read retry function tries up to 15 times to get a sensor reading,
    # with 2-second wait between retries

    if humidity is not None and temperature is not None: # if both temp & humidity are ok...
        print("Temp={0:0.1f}*C Humidity = {1:0.1f}%".format(temperature, humidity))
        # printed as "Temp = 25.2*C Humidity = 56.7%" for instance
    
    else:
        print("Failed to get reading. Try again!")

    sleep(2)


# Push Button, LED Lights & Buzzer

import RPi.GPIO as GPIO #Imports RPi’s GPIO module and call that GPIO.
from time import sleep 

GPIO.setmode(GPIO.BCM) # Pin 13 is also GPIO 27. This line says refer to the pins using their GPIO numbers. # Broadcom Mode since we are using the Broadcom chipset
GPIO.setwarnings(False) # To get rid of warning, if the GPIO pins you are using have been used before.
GPIO.setup(27, GPIO.OUT) # Make GPIO 27 an output pin. (RED)
GPIO.setup(22, GPIO.OUT) # Make GPIO 22 an output pin. (YELLOW)
GPIO.setup(26, GPIO.OUT) # Make GPIO 26 an output pin. (GREEN)
GPIO.setup(17, GPIO.OUT) # Make GPIO 17 an output pin. (buzzer)
GPIO.setup(19, GPIO.IN) # Make GPIO 19 an input pin. (push button)

"""
The green LED should light up for 15 sec, followed by
the yellow LED for 2 sec, followed by the red LED for 10
sec. The buzzer should beep (on and off) at 1 sec
interval when the red LED is lighting up ( we don’t
have a “green man” which should light up when the red
LED is lighting up). Pressing the button will cause the
green LED’s time to be reduced to 10 sec.

"""

while(True):
    
    print("GREEN LED turns on...")
    GPIO.output(27,0) # RED LED turns on
    GPIO.output(22,0) # YELLOW LED turns on
    GPIO.output(26,1) # Green LED turns on

    # timer for GREEN LED (10-15 secs)
    count = 0
    max = 15 # can use 150 here
    while (count < max):
        if (GPIO.input(19)):
            print("PUSH Button Pressed. Green LED Time Reduced...")
            max = 10 # and 100 here
        sleep(1) # and 0.1 here

        count+=1
    
    GPIO.output(27,0) # RED LED turns off
    GPIO.output(22,1) # YELLOW LED turns off
    GPIO.output(26,0) # Green LED turns off
    print("GREEN LED turns off...")
    print("YELLOW LED turns on for 2 secs...")
    sleep(2)

    """for x in range(2): 
        GPIO.output(22,1) # Yellow LED turns on
        sleep(1)
    """
    
    GPIO.output(27,1) # RED LED turns ON
    GPIO.output(22,0) # YELLOW LED turns off
    print("YELLOW LED turns off...")
    GPIO.output(26,0) # Green LED turns off
    print("RED LED turns on for 10 secs...")
    
    for x in range(10):
        GPIO.output(17,1) # Buzzer turns on
        sleep(0.5)
        GPIO.output(17,0) # Buzzer turns off
        sleep(0.5)

# Print Time
import time
print(time.strftime("%H:%M:%S"))
print(time.strftime("%d/%m/%Y"))

# Collect Time
from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)

# Importing Temp & Humidity into CSV
# collecting data from the temperature, humidity sensor and saving it into a CSV file
import Adafruit_DHT
import time
from time import sleep
import csv

sensor = Adafruit_DHT.AM2302 # refer to AM2302 as "temperature and humidity sensor"
pin = 4 # sensor output connected to GPIO 4
row = 0 # Declare row to store the "row number" and initialise it.

while (True):
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    # read retry function tries up to 15 times to get a sensor reading,
    
    if humidity is not None and temperature is not None: # if both temp & humidity are ok...
        print("Temp={0:0.1f}*C Humidity = {1:0.1f}%".format(temperature, humidity))
        # printed as "Temp = 25.2*C Humidity = 56.7%" for instance

        # construct a row of data, consisting of row (sample number), temperature & humidty, time & date
        row+=1 # increment the row number
        row_time = time.strftime("%H:%M:%S") #date and time settings
        row_date = time.strftime("%d/%m/%Y")
        data_row = [row, int(temperature), int(humidity), row_time, row_date] # construct a row of data for the CSV file

        # open csv file & append the row of data
        with open('sensordata.csv', 'a') as file_handle:
            data_file = csv.writer(file_handle, delimiter=",", lineterminator="\n")
            # use the writer function to append rows of data, using comma as delimiter and newline as the line terminator
            data_file.writerow(data_row) # use the writerow function to add a row of data to the file
        
    else:
        print("Failed to get reading. Try again!")

    sleep(2)


# Download data from Thingspeak to display
import requests
import json

# previously uploaded values
# temperature = [23,24,25,23,21,22,24,26,27,26]
# humidity    = [55,57,60,59,62,66,70,68,66,65]

resp = requests.get("https://api.thingspeak.com/channels/1930750/feeds.json?results=10") # read all fields, 10 values
# resp = requests.get("https://api.thingspeak.com/channels/1930750/fields/2.json?results=10") # to read only field 2, 10 values

print(resp.text) # comment out this line, if you don't want to see what is in the json object

results=json.loads(resp.text) # convert json into Python Object

for x in range(10):
    print (f"Downloaded sample {x}: temperature =", results["feeds"][x]["field1"], ", humidity = ", results["feeds"][x]["field2"])
    # you will understand this line once we use an online json viewer to see what is inside the "results"


# Upload Data into Thingspeak
import time
import requests

temperature = [23,24,25,23,21,22,24,26,27,26]
humidity    = [55,57,60,59,62,66,70,68,66,65]

for x in range(10):
    print(f"Uploading sample {x}...") 
    resp = requests.get("https://api.thingspeak.com/update?api_key=VTZ7RZFVOMRBIXK4&field1=%s&field2=%s" %(temperature[x], humidity[x])) # update a channel feed
    # requests.get is used to send data to cloud
    # eacg iteration in the for loop uploads a temperature value & a humidity value
    time.sleep(20) # an interval of at least 15 seconds is required, for uploading to a free channel


# IR (PIR) Sensor
import RPi.GPIO as GPIO #import RPi.GPIO module
from time import sleep
GPIO.setmode(GPIO.BCM) #choose BCM mode
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.IN) # set GPIO 17 as input

sleep(5) #to allow sensor time to stabilize
PIR_state=0 #use this, so that only a change in state is reported

while (True):
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


# DC Motor On & Off
import RPi.GPIO as GPIO #import RPi.GPIO module
from time import sleep

GPIO.setmode(GPIO.BCM) #choose BCM mode
GPIO.setwarnings(False)
GPIO.setup(23,GPIO.OUT) #set GPIO 23 as output

while True: #loops the next 4 lines
    GPIO.output(23,1) #output logic high/'1'
    sleep(1) #delay 1 second
    GPIO.output(23,0) #output logic low/'0'
    sleep(1) #delay 1 second


# DC Motor Speed Control
import RPi.GPIO as GPIO #import RPi.GPIO module
from time import sleep

GPIO.setmode(GPIO.BCM) #choose BCM mode
GPIO.setwarnings(False)
GPIO.setup(23,GPIO.OUT) #set GPIO 23 as output
PWM = GPIO.PWM(23,100) #set 100Hz PWM output at GPIO 23

while True: #loops the next 3 lines
    for i in range(0,101,25):
        PWM.start(i)
        sleep(0.5)


# Servo Motor 
import RPi.GPIO as GPIO #import RPi.GPIO module
from time import sleep

GPIO.setmode(GPIO.BCM) #choose BCM mode
GPIO.setwarnings(False)
GPIO.setup(26,GPIO.OUT) #set GPIO 26 as output
PWM=GPIO.PWM(26,50) #set 50Hz PWM output at GPIO26

while (True):
    PWM.start(3) #3% duty cycle
    print('duty cycle:', 3) #3 o'clock position
    sleep(4) #allow time for movement
    PWM.start(13) #13% duty cycle
    print('duty cycle:', 13) #9 o'clock position
    sleep(4) #allow time for movement


# LCD Display (Line)
import I2C_LCD_driver #import the library
from time import sleep

LCD = I2C_LCD_driver.lcd() #instantiate an lcd object, call it LCD
sleep(0.5)
LCD.backlight(0) #turn backlight off
sleep(0.5)
LCD.backlight(1) #turn backlight on
LCD.lcd_display_string("LCD Display Test", 1) #write on line 1
LCD.lcd_display_string("Address = 0x27", 2, 2) #write on line 2

#starting on 3rd column
sleep(2) #wait 2 sec
LCD.lcd_clear() #clear the display


# RFID Reader (there are 3 sample codes 
# (Clear Database.py, Register Cards.py, Identify Cards.py), a database file (authlist.txt), 
# and a library folder (mfrc522, which contains _init_.py, MFRC522.py, SimpleMFRC522.py))


# Media+Voice Playback (https://www.geeksforgeeks.org/vlc-module-in-python-an-introduction/)

# importing vlc module
import vlc
 
# creating vlc media player object
media = vlc.MediaPlayer("filename.mp3")
 
# start playing video
media.play()

# Keypad
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

MATRIX=[ [1,2,3],
         [4,5,6],
         [7,8,9],
         ['*',0,'#']] #layout of keys on keypad
ROW=[6,20,19,13] #row pins
COL=[12,5,16] #column pins

#set column pins as outputs, and write default value of 1 to each
for i in range(3):
    GPIO.setup(COL[i],GPIO.OUT)
    GPIO.output(COL[i],1)

#set row pins as inputs, with pull up
for j in range(4):
    GPIO.setup(ROW[j],GPIO.IN,pull_up_down=GPIO.PUD_UP)

#scan keypad
while (True):
    for i in range(3): #loop thru’ all columns
        GPIO.output(COL[i],0) #pull one column pin low
        for j in range(4): #check which row pin becomes low
            if GPIO.input(ROW[j])==0: #if a key is pressed
                print (MATRIX[j][i]) #print the key pressed
                while GPIO.input(ROW[j])==0: #debounce
                    sleep(0.1)
        GPIO.output(COL[i],1) #write back default value of 1

