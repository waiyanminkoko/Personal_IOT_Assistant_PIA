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
