import pandas as pd
table = pd.read_csv('bank-data.csv', delimiter=",")
print(table)
df = pd.DataFrame(table)
jobtable = pd.DataFrame(df["job"]) 
jobtable['job']
check = input()
for i in jobtable['job']:
    if i.casefold() == check.casefold(): #CASE-INSENSITIVE
        message = 'access granteed'
        
    else : 
        pass
print(message)


#checking for min max age
agetable = pd.DataFrame(df["age"])
print(agetable['age'])
ages = list(agetable['age'])
max_age = max(ages)
min_age = min(ages)
age_dict = {'min-age' : min_age , 'max-age': max_age}
print(age_dict)

