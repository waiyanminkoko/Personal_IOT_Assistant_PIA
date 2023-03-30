# TWI_LCD
# VCC to 5V e.g pin 2
# SDA to SDA1 i.e pin 3 or GPIO2
#SDL to SCL1 i.e pin 5 or GPIO3
# GND to GND e.g pin 6

import I2C_LCD_driver
from time import *

mylcd = I2C_LCD_driver.lcd() # create an instance & call it mylcd
while (True):
    mylcd.lcd_display_string("Enter password (*****):", 1, 1) # line 1, position 1
    for i in range(5):
        mylcd.lcd_display_string("*",2, i) # line 2, positions 1 to 4
        # read the character entered - see keypad program
        sleep(1)
    mylcd.lcd_clear() # clear display
    sleep(5)