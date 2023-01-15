import pandas as pd
from datetime import datetime

url = 'https://api.thingspeak.com/channels/2007583/fields/1/last.csv'
df = pd.read_csv(url)
date_time = df['created_at'].iloc[0]
get_date_time = datetime.strptime(date_time, '%Y-%m-%dT%H:%M:%S%z')
last_date_time_entry = get_date_time.strftime('%Y-%m-%d %H:%M:%S')
print(last_date_time_entry)
