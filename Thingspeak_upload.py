import time
import requests

temperature = [23,24,25,23,21,22,24,26,27,26]
humidity    = [55,57,60,59,62,66,70,68,66,65]

for x in range(10):
    print(f"Uploading sample {x}...") 
    resp = requests.get("https://api.thingspeak.com/update?api_key=08MM0FTOM82Y4N4R&field1=%s&field2=%s" %(temperature[x], humidity[x])) # update a channel feed
    # requests.get is used to send data to cloud
    # eacg iteration in the for loop uploads a temperature value & a humidity value
    time.sleep(20) # an interval of at least 15 seconds is required, for uploading to a free channel