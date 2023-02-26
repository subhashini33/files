import pandas as pd
  
# reading two csv files
data1 = pd.read_csv('data\locations.csv')
data2 = pd.read_csv('data\location_temp.csv')
  
# using merge function by setting how='inner'
#df_final = data1.merge(data2, left_on = 'city name', right_on = 'city')
output1 = pd.merge(data1, data2, 
                   left_on='city name',right_on='city',
                   how='inner')
output1 = output1.drop("city",axis=1)
# displaying result
print(output1)