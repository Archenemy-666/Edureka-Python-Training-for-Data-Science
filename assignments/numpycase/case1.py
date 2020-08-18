#Extract data from the givenSalaryGender CSV file 
# and store the data from each column in a separate NumPy array
import pandas as pd 
import numpy as np 
table  = pd.read_csv("SalaryGender.csv")
df = pd.DataFrame(table)

salary = np.array(df['Salary'])
gender = np.array(df['Gender'])
age = np.array(df['Age'])
phd = np.array(df['PhD'])



#1. The number of men with a PhD
# 2. The number of women with a PhD
filtered = df[(df['Gender'] == 1) & (df['PhD'] == 1)]
filtered_men = df[(df['Gender'] == 0) & (df['PhD'] == 1)]
print(filtered)
countw = 0
countm = 0
for line in filtered['Gender'] : 
    countw = countw + 1
for line in filtered_men['Gender'] : 
    countm = countm + 1
print("women with phd : ",countw)
print("men with phd : ",countm)


#Use SalaryGender CSV file. Store the “Age” and “PhD” columns 
# in one DataFrame and delete the data of all people who don’t have a PhD
#Calculate the total number of people who have a PhD degreefrom SalaryGender CSV file.
age_phd = pd.DataFrame()
age_phd['age']=pd.Series(df['Age'])
age_phd['phd']=pd.Series(df['PhD'])
answer = age_phd[age_phd['phd']==1]
answer
answer.count()

#How  do  you  Count  The  Number  Of  Times  Each  Value 
# Appears  In  An  Array  Of Integers?[0, 5, 4, 0, 4, 4, 3, 0, 0, 5, 2, 1, 1, 9]
array1 = pd.DataFrame()
array1 = pd.Series([0, 5, 4, 0, 4, 4, 3, 0, 0, 5, 2, 1, 1, 9])
array1.value_counts()

#Create a numpyarray[[0, 1, 2],[ 3, 4, 5],[ 6, 7, 8],[ 9,10, 11]]) 
# and filter the elements greater than 5.

array2 = np.array([[0, 1, 2],[ 3, 4, 5],[ 6, 7, 8],[ 9,10, 11]])
array2
for i in range(0,3):
    for j in range(0,3):
        if array2[i,j] > 5:
            array2[i,j] = 0
print(array2)

#Create a numpy array having NaN (Not a Number) and print it.
# array([ nan,   1.,   2.,  nan,   3.,   4.,   5.])
# Print the same array omitting all elements which are nan
import numpy as np
array3 = np.array([np.nan,1,2,np.nan,3,4,5])
array3 = np.delete(array3,(0,3))
array3

#Create  a  10x10  array  with  random  values  
# and  find  the  minimum  and  maximum values.
from random import randint
import numpy as np 
array4 = np.empty((10,10))
for i in range(0,10):
    for j in range(0,10):
        array4[i,j] = randint(0,40)
print(array4)
array4.max()
array4.min()

#Create a random vector of size 30 and find the mean value.
array5 = np.empty((7))
for j in range(0,6):
    array5[j]=randint(0,40)
np.mean(array5)
#Create numpy array having elements 0 to 10
#  And negate all the elements between 3 and 9
array6 = np.empty(10)
for i in range(0,9):
    array6[i] = randint(1,20)
array6[3:10] = -array6[3:10]
array6
#Create a random array of 3 rows and 3 columns 
# and sort it according to 1st column, 2nd column or 3rd column.
import random
array7 = np.random.rand(3,3)
np.sort(array7)

#Create a random array and swap two rows of an array
swap = np.random.rand(2,5)
print(swap)
swap[0]
swap[1]
swap[[0, 1],:] = swap[[1, 0],:]
print(swap)
#--------------------------------------------------------------------------------------------------------------
#15 question 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns
schoool_table = pd.read_csv('middle_tn_schools.csv',delimiter=',')
df = pd.DataFrame(schoool_table)
#schools with rating 0 arent qualified to be part of the table 
updated = df[df['school_rating'] >= 1.0]    
updated
df.describe()
x = np.array(df['school_rating'])
y = np.array(df['size'])
print("rating vs size")
print(plt.scatter(y,x))

print("student to techer ratio vs rating")
z = np.array(df['stu_teach_ratio'])
plt.xlim(0,30)
print(plt.scatter(z,x))

print("student to techer ratio vs rating")
z = np.array(df['reduced_lunch'])
print(plt.scatter(z,x))

relation = df[['reduced_lunch','school_rating']]
relation
rel = relation.corr()
rel

group1 = df.groupby(['school_rating']).groups
print(group1)
group1.describe()

cor = df.corr()
print(cor)
sns.heatmap(cor,square = True,cmap = "YlGnBu")

