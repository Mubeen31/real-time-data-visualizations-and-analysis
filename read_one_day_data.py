import pandas as pd
import urllib.request
import json
import time

url = 'https://api.thingspeak.com/channels/2007583/fields/2.csv?results=50'
url1 = 'https://api.thingspeak.com/channels/2007583/fields/2.csv?days=2'
url2 = 'https://api.thingspeak.com/channels/9/fields/1.csv?start=2023-01-14%2023:01:14&end=2023-01-14%2023:01:14'

df = pd.read_csv(url2)
print(df)
