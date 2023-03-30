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
