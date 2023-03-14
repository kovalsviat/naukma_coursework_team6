

# ### Script for the weather API
# #### to get the weather forecast for next 12 hours

import urllib.request
import sys
import datetime
import json
import pytz
import pandas as pd             

BASE_URL = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline"
API_KEY = ""
location = "Kyiv,Ukraine"

date_now = datetime.datetime.now(pytz.timezone('Europe/Kyiv')).strftime("%Y-%m-%d")
time_now_wout = datetime.datetime.now(pytz.timezone('Europe/Kyiv')).strftime("%H:%M")
time_now = f"{time_now_wout}:00"
#print(date_now, time_now)
time_end = "23:00:00"

url = f"{BASE_URL}/{location}/{date_now}T{time_now}/{date_now}T{time_now}?key={API_KEY}&include=hours&unitGroup=metric&contentType=json"
url

try: 
  ResultBytes = urllib.request.urlopen(url)
  
  # Parse the results as JSON
  jsonData = json.load(ResultBytes)

        
except urllib.error.HTTPError  as e:
  ErrorInfo= e.read().decode() 
  print('Error code: ', e.code, ErrorInfo)
  sys.exit()
except  urllib.error.URLError as e:
  ErrorInfo= e.read().decode() 
  print('Error code: ', e.code,ErrorInfo)
  sys.exit()

