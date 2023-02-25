import requests
import pandas as pd
df=pd.read_csv('data/locations.csv')
df
print(df)
hourly_data = pd.DataFrame()

for i,row in df.iterrows():
    print(row['latitude'])
    url = f"https://api.open-meteo.com/v1/forecast?latitude={row['latitude']}&longitude={row['latitude']}&current_weather=true&hourly=temperature_2m,relativehumidity_2m,windspeed_10m"
    print(row['city name'],url)


    resp=requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={row['latitude']}&longitude={row['latitude']}&current_weather=true&hourly=temperature_2m,relativehumidity_2m,windspeed_10m")
    # print(resp)
    # df1=pd.DataFrame(resp)
    # print(df1)
    data=resp.json()
    hourly_data_temp = pd.DataFrame(data['hourly'])
    hourly_data_temp['city'] = row['city name']
    #print(hourly_data)
    hourly_data = pd.concat([hourly_data,hourly_data_temp],axis=0)
    
#print(hourly_data)
print(hourly_data.city.value_counts())

hourly_data.to_csv('data/location_temp.csv',index=False,header=False)

