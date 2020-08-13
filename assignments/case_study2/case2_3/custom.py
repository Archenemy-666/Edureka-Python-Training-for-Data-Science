import pandas as pd 
import re
table = pd.read_csv('FairDealCustomerData.csv',delimiter=',',header=None)
df = pd.DataFrame(table)
print(df)
df[1]
df.dropna(inplace = True)
namesplit = df[1].str.split(' ',n=3,expand = True)
print(namesplit)
df['honorifics'] = namesplit[1]
df['firstname'] = namesplit[2]
df['lastname'] = namesplit[3]
df.drop(columns= [0],inplace = True)
df.drop(columns = [1], inplace= True)
df.to_csv('newradings.csv')







