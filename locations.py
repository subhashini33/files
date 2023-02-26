import requests
import pandas as pd
# Read csv data as pandas datframe
df=pd.read_csv('data/locations.csv')
print(df)
# output empty dtaframe creation It will be updated inside loop
hourly_data = pd.DataFrame()

# row  wise (for ecah location) iteration
# df.iterrows will retun iterator object of type tuple
# with in loop i is the index of df
# row is a pandas Series 
for i,row in df.iterrows():
    print(row['latitude'])
    # creating url using lattitude and longitude in teh row
    url = f"https://api.open-meteo.com/v1/forecast?latitude={row['latitude']}&longitude={row['longitude']}&current_weather=true&hourly=temperature_2m,relativehumidity_2m,windspeed_10m"
    print(row['city name'],url)

    # API get request to fetch waether data for given location 
    resp=requests.get(url)
    # print(resp)
    # df1=pd.DataFrame(resp)
    # print(df1)
    # We need only ['time', 'temperature_2m', 'relativehumidity_2m', 'windspeed_10m'] under hourly key in the api response.
    data=resp.json()
    # creating dataframe with above mentioned columns from a dict
    hourly_data_temp = pd.DataFrame(data['hourly'])
    #hourly_data_temp  will have  ['time', 'temperature_2m', 'relativehumidity_2m', 'windspeed_10m'] 
    # deriviing city column from csv rowdata
    hourly_data_temp['city'] = row['city name']
    #hourly_data_temp  will have  ['time', 'temperature_2m', 'relativehumidity_2m', 'windspeed_10m','city'] 
    #print(hourly_data)
    # concatenate the data with previous final data in the hourly_data for first row iteration hourly data is an empty dataframe
    hourly_data = pd.concat([hourly_data,hourly_data_temp],axis=0)
    
#print(hourly_data)
# To cross check whether all the locations are present or not in the final result.
print(hourly_data.city.value_counts())

# write the final result with all locations horly data into csv file  without index and with header
hourly_data.to_csv('data/location_temp.csv',index=False,header=True)

