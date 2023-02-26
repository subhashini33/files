import requests
import pandas as pd
df=pd.read_csv('data/locations.csv')
# print(df)
for i,row in df.iterrows():
    #print(row['latitude'])
    url = f"https://api.open-meteo.com/v1/forecast?latitude={row['latitude']}&longitude={row['longitude']}&current_weather=true&hourly=temperature_2m,relativehumidity_2m,windspeed_10m"
    # print(row['city name'],url)


    resp=requests.get(url)
    data=resp.json()
    hourly_data_tmp = pd.DataFrame(data['hourly'])
    
    if i==0:
        hourly_data_tmp = hourly_data_tmp[['time','temperature_2m']] 
        hourly_data = hourly_data_tmp.rename({'temperature_2m':row['city name']},axis=1)
    else:
        hourly_data[row['city name']] = hourly_data_tmp['temperature_2m']
    print(hourly_data)