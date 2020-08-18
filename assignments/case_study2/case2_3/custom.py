import pandas as pd 
import re
from customerdata import CustomerData
#storing data in class
data = CustomerData('FairDealCustomerData.csv')
data.get_file('FairDealCustomerData.csv')


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
file1 = pd.read_csv('newradings.csv')
name = input("input first name or last name : ")
namesplit[2][0]
'''
for i in range(2,4):
    for j in range(len(namesplit[2])):
        if ((namesplit[i][j]) == name):
            print('present')
            x = 1
        else :
            print(...)
            x = 'None'
print(x)
    print("everuthings cool",x/1)
'''
# checking for the value
name = input("input first name or last name : ")
result = namesplit.isin([name])
listOfPos = []
section = result.any()
columnNames = list(section[section == True].index)
for col in columnNames: 
        rows = list(result[col][result[col] == True].index) 
  
        for row in rows: 
            listOfPos.append((row, col))
#try except
try:
    x = listOfPos[0]
    print("element at : ",listOfPos)
except:
    print("customer invalid")          

