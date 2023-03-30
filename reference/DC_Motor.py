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