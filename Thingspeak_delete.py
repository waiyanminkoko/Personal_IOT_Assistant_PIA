import time
import requests
import webwrite

ChannelID = 1971834
UserAPIKey = 'Q581CKBP8SUI2A3L'; # This is available from https://thingspeak.com/account/profile
url = 'https://api.thingspeak.com/channels/1971834/feeds.json?api_key=Q581CKBP8SUI2A3L'
response = webwrite(url, weboptions('RequestMethod','delete'))