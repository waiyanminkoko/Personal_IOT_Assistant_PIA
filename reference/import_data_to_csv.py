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

