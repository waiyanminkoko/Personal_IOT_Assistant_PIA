from flask import Flask, render_template,request, redirect
from mfrc522 import SimpleMFRC522

import sys

import spidev
my_spi = spidev.SpiDev()
my_spi.open(0,0)

# set up for controlling LED (digital output)
import RPi.GPIO as GPIO
# set up for reading temperature and humidity values
# set up ThingSpeak

import dht11 # Temp & Humidity Sensor

# General
import datetime
import requests
from datetime import *
from time import *
now = datetime.now()

import I2C_LCD_driver

# VLC
import vlc
from vlc import *
import glob
import vlc_music
from vlc_music import *

# GPIO BUTTONS LED BUZZER
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(4,GPIO.OUT) # DC Motor
GPIO.setup(24, GPIO.OUT) # Make GPIO 24 an output pin. (LED)
GPIO.setup(18, GPIO.OUT) # Make GPIO 19 an input pin. (buzzer)
GPIO.setup(17, GPIO.IN) # Make GPIO 17 an output pin. (PIR - Passie Infrared)
GPIO.setup(22,GPIO.IN) #set GPIO 22 as input (Slide Switch)

# RFID Setup
"""reader = SimpleMFRC522()
auth = []
id = reader.read_id()
id = str(id)"""


# GPIO MOTORS
GPIO.setup(23,GPIO.OUT) #set GPIO 23 as output (DC Motor)
GPIO.setup(26,GPIO.OUT) #set GPIO 26 as output (Servo Motor)
Servo_pin = 26
DC_pin = 23
PWM_servo = GPIO.PWM(26,50) #set 50Hz PWM output at GPIO26
PWM_servo.start(0)
PWM_dc = GPIO.PWM(23,100) #set 100Hz PWM output at GPIO 23
PWM_dc.start(0)

servo_position = 0
motor_speed = 0

LCD = I2C_LCD_driver.lcd() #instantiate an lcd object, call it LCD

app = Flask(__name__) # __name__ = name of the current file


# Uploading Temp and Humidity Data to ThingSpeak

API_KEY = "<08MM0FTOM82Y4N4R>"
CHANNEL_ID = "<1971834>"

temperature = 0.0
humidity = 0.0

def send_data_to_thingspeak():
    global temperature, humidity
    global result
    # update the temperature and humidity variables
    instance = dht11.DHT11(pin=21)
    result = instance.read()
    if result.is_valid():
        temperature = result.temperature
        humidity = result.humidity
    try:
        # send the data to ThingSpeak
        response = requests.get("https://api.thingspeak.com/update?api_key=08MM0FTOM82Y4N4R&field1=%s&field2=%s"%(temperature, humidity)) # update a channel feed
        # check if the request was successful
        if response.status_code == 200:
            print("Data sent to ThingSpeak successfully")
        else:
            print("Failed to send data to ThingSpeak. (Try Condition)")
    except:
        print("Failed to send data to ThingSpeak (Except Condition)")

def update_thingspeak_data():
    send_data_to_thingspeak()
    #time.sleep(15)

import threading

thread = threading.Thread(target=update_thingspeak_data)
thread.start()

resp = requests.get("https://api.thingspeak.com/update?api_key=08MM0FTOM82Y4N4R&field1=%s&field2=%s"%(temperature, humidity)) # update a channel feed
time.sleep(15) # an interval of at least 15 seconds is required, for uploading to a free channel

"""
# code for automatically RFID Detection
"""
"""
# get duty cycle of the Motors
def get_dutycycle(pin, PWM):
    dutycycle = 0
    PWM = GPIO.setup(pin, GPIO.OUT)
    # Get the current duty cycle
    dutycycle = PWM.ChangeDutyCycle(dutycycle)
    # Clean up the GPIO setup
    GPIO.cleanup()
    return dutycycle

"""

@app.route("/")  # default location of the file also automatically run the python programs we want (Sensors and state of switches)
def index():
    #update_thingspeak_data()
    # temp & humidity sensor

    instance = dht11.DHT11(pin=21) #read data using pin 21
    result = instance.read()


    if result.is_valid():
        #result = instance.read()
        temperature = result.temperature
        humidity = result.humidity

    # check light status
    light_status = GPIO.input(24)
    servo_position= GPIO.input(26)
    motor_speed = GPIO.input(23)
        # check servo_position for curtain
    if servo_position:
        servo_state = "OPEN"
    else:
        servo_state = "CLOSE"
        # check motor_speed for Fan Speed
    
    if (motor_speed == 0):
        motor_state = "OFF"
    elif (motor_speed > 0 and motor_speed <=25):
        motor_state = "LOW"
    elif (motor_speed > 25 and motor_speed <=50):
        motor_state = "MEDIUM"
    else:
        motor_state = "HIGH"
        
        #return render_template("index.html", servo_state=servo_state)
        #return render_template("index.html", servo_position=servo_position)
        #return render_template("index.html", motor_state=motor_state)
        #return render_template("index.html", light_status=light_status)

    return render_template("home.html", #temperature=temperature, humidity=humidity, 
    light_status=light_status, servo_position=servo_position, servo_state=servo_state, 
    motor_speed = motor_speed, motor_state= motor_state)

    # return render_template("home.html") # print it to the user screen

@app.route("/PLAY_MUSIC")
def VLC_PLAYER_PLAY():
    play = 1
    playmusic(play)
    return redirect("/")

@app.route("/STOP_MUSIC")
def VLC_PLAYER_STOP():
    play = 0
    playmusic(play)
    return redirect("/")

@app.route("/LED_is_OFF")
def show_LED_is_OFF():
    GPIO.output(24,0) # turn off the physical LED
    sleep(1)
    #return render_template("home.html")
    return redirect("/")

@app.route("/LED_is_ON")
def show_LED_is_ON():
    # temp_val=str(read_temphumi()) 
    GPIO.output(24,1) # turn on the physical LED
    sleep(1)
    return redirect("/")

@app.route("/Curtain_CLOSE")
def Curtain_is_CLOSE():
    # PWM_servo.ChangeDutyCycle(2) #0 degree
    PWM_servo.start(3) #0 degree
    time.sleep(2)
    #PWM_servo.stop()
    servo_position = 1
    return redirect("/")

@app.route("/Curtain_OPEN")
def Curtain_is_OPEN():
    # PWM_servo.ChangeDutyCycle(12) #180 degree
    PWM_servo.start(12) #180 degree
    time.sleep(2)
    
    #PWM_servo.stop()
    servo_position = 0
    return redirect("/")

@app.route("/Fan_OFF")
def Fan_is_OFF():
    PWM_dc.ChangeDutyCycle(0) # DC Motor OFF
    PWM_dc.stop() 
    motor_speed = 0
    return redirect("/")

@app.route("/Fan_ON")
def Fan_is_ON():
    PWM_dc.ChangeDutyCycle(50) #DC Motor
    PWM_dc.start(50)
    motor_speed = 50
    return redirect("/")

@app.route("/Fan_LOW")
def Fan_is_LOW():
    PWM_dc.ChangeDutyCycle(50) #DC Motor
    motor_speed = 25
    PWM_dc.start(50)
    #return render_template("home.html")
    return redirect("/")

@app.route("/Fan_MEDIUM")
def Fan_is_MEDIUM():
    PWM_dc.ChangeDutyCycle(75) #DC Motor
    motor_speed = 50
    PWM_dc.start(75)
    #return render_template("home.html")
    return redirect("/")

@app.route("/Fan_HIGH")
def Fan_is_HIGH():
    PWM_dc.ChangeDutyCycle(100) #DC Motor
    motor_speed = 100
    PWM_dc.start(100)
    #return render_template("home.html")
    return redirect("/")


@app.route("/Morning")
def Test_Morning():
    snooze = 0
    play = 1
    current_route = "MORNING"
    # LCD Display
    # LCD.lcd_display_string(str(datetime.now().time()), 1, 1)
    LCD.lcd_display_string(time.strftime("%H:%M:%S"), 1, 1)
    LCD.lcd_display_string("GOOD MORNING(>U<)", 2, 2)

    
    # BUZZER
    while (snooze == 0):
        GPIO.output(18,1) # Buzzer
        sleep(0.5)
        if (GPIO.input(22)):
            GPIO.output(18,0)
            snooze += 1
        GPIO.output(18,0) # Buzzer
        sleep(0.5)
        if (GPIO.input(22)):
            GPIO.output(18,0)
            snooze += 1
    # LIGHT
    GPIO.output(24,1)

    # Curtain
    PWM_servo.start(12) #12% duty cycle
    sleep(2)
    PWM_servo.stop()

    #DC Motor
    PWM_dc.start(100)
    motor_speed = 50

    #VLC PLAYER 
    playmusic(play) # from vlc_music.py

    # PWM_servo.stop()

    return render_template("home.html", current_route = current_route)

@app.route("/Bye") # This page isn’t working 0.0.0.0 didn’t send any data.
                    # ERR_EMPTY_RESPONSE
def Test_Bye():
    current_route = "BYE"
    play = 0
    # LIGHT
    GPIO.output(24,0)

    # DC Motor / FAN
    PWM_dc.start(0)
    motor_speed = 0

    playmusic(play)
    return render_template("home.html", current_route = current_route)

@app.route("/Night")
def Test_Night():
    current_route = "NIGHT"
    #LCD.lcd_display_string(time.strftime("11:23AM %H:%M:%S"), 1, 1)
    # mylcd.lcd_display_string(str(datetime.now().time()), 1, 1)
    #LCD.lcd_display_string("GOOD EVENING(>U<)", 2, 2)
    play = 1

    # LIGHT
    GPIO.output(24,1)

    # Curtain
    PWM_servo.start(2) #2% duty cycle
    sleep(2)
    PWM_servo.stop()

    # DC Motor / FAN
    PWM_dc.start(100)
    motor_speed = 50

    #VLC PLAYER 
    playmusic(play) # from vlc_music.py

    return render_template("home.html", current_route = current_route)
    
@app.route("/Sleep")
def Test_Sleep():
    current_route = "SLEEP"

    # LIGHT
    GPIO.output(24,0)

    # Curtain
    PWM_servo.start(2) #2% duty cycle
    sleep(2)
    PWM_servo.stop()

    # DC Motor / FAN
    PWM_dc.start(0)
    motor_speed = 0

    return render_template("home.html", current_route = current_route)

@app.route("/Auto")
def Test_Auto():
    current_route = "AUTO"

    return render_template("home.html", current_route = current_route)

# other "Web Pages not shown"
if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0") # 0.0.0.0 => accessible to any device on the network