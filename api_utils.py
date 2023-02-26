# import requests
# import pandas as pd
# resp = requests.get('https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=12.41&current_weather=true&hourly=temperature_2m,relativehumidity_2m,windspeed_10m')
# print(resp.status_code)
# data = resp.json()
# print(type(data))
# print(data.keys())
# print(data['current_weather'].keys())
# print(data['current_weather']['temperature'])
# print(data['hourly'].keys())
# print(len(data['hourly']['time']))
# #print(data['hourly']['time'])
# # ['time', 'temperature_2m', 'relativehumidity_2m', 'windspeed_10m']
# hourly_data = pd.DataFrame(data['hourly'])
# print(hourly_data)
# hourly_data['city'] = 'india'
# print(hourly_data)


import requests
import pandas as pd
df=pd.read_csv('data/locations.csv')


for i,row in df.iterrows():
    #print(row['city name'],end=" ")
    url = f"https://api.open-meteo.com/v1/forecast?latitude={row['latitude']}&longitude={row['longitude']}&current_weather=true&hourly=temperature_2m,relativehumidity_2m,windspeed_10m"
    # print(row['city name'],url)


    resp=requests.get(url)
    
    data=resp.json()
    hourly_data_tmp = pd.DataFrame(data['hourly'])
    print(hourly_data_tmp)
    if i==0:
        hourly_data_tmp = hourly_data_tmp[['time','temperature_2m']]        
        hourly_data = hourly_data_tmp.rename({'temperature_2m':row['city name']},axis=1)
    else:
        hourly_data[row['city name']] = hourly_data_tmp['temperature_2m']
    
    print(hourly_data)
hourly_data.to_csv('data/location_temp2m_.csv',index=False,header=True)
hourly_data.to_json('data/location_temp2m_.json')

    
    #['time', 'temperature_2m', 'relativehumidity_2m', 'windspeed_10m']

    # # print(resp)
    # # df1=pd.DataFrame(resp)
    # # print(df1)
    # data=resp.json()
    # hourly_data_temp = pd.DataFrame(data['city name'])
    # print(hourly_data)








