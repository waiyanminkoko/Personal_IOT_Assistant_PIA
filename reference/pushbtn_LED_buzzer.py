# Push Button, LED Lights & Buzzer

import RPi.GPIO as GPIO #Imports RPi’s GPIO module and call that GPIO.
from time import sleep 

GPIO.setmode(GPIO.BCM) # Pin 13 is also GPIO 27. This line says refer to the pins using their GPIO numbers. # Broadcom Mode since we are using the Broadcom chipset
GPIO.setwarnings(False) # To get rid of warning, if the GPIO pins you are using have been used before.
GPIO.setup(24, GPIO.OUT) # Make GPIO 24 an output pin. (LED)
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
    GPIO.output(24,1) #output logic high/'1'
    sleep(1) #delay 1 second
    GPIO.output(24,0) #output logic low/'0'
    sleep(1) #delay 1 second
    
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
