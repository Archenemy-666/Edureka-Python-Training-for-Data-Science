import os 
import pandas as pd

x = pd.read_csv('bank-data.csv')
print(x.job)
type(x.job)
list1 = [x.job]
print(list1)
map(str,list1)
print(list1)
type(list1)
for i in list1:
    print(type(i))
management = 0
admin = 0
blue_collar = 0
entre = 0
housemaid = 0
management = 0
selfem = 0
for i in x.job:
    if(i == 'management'):
        management = management + 1
    elif(i == 'admin.'):
        admin = admin + 1
    elif(i == 'blue-collar'):
        blue_collar = blue_collar + 1
    elif(i == 'entrepreneur'):
        entre = entre + 1 
    elif(i == 'housemaid'):
        housemaid = housemaid + 1
    elif(i == 'management'):
        management = management + 1
    elif(i == 'self-employed'):
        selfem = selfem + 1 
        
print("management count",management)
print("admin count : ",admin)
print("blue_coller count : ",blue_collar)
print("entrepreneur count : ",entre)
print("")

