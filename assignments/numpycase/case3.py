import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
from random import randint
read = pd.read_csv('Hurricanes.csv')
df = pd.DataFrame(read)
y  = np.array(df['Year'])
x = np.array(df['Hurricanes'])
plt.bar(x,y)
plt.xlabel('Year')
plt.ylabel('Hurricanes')

read1 = pd.read_csv('CityTemps.csv')
df1 = pd.DataFrame(read1)
y = np.array(df1['San Francisco'])
z = np.array(df1['Moscow'])
plt.hist(y)
plt.hist(z)

x = np.array([1,2,3,4])
y = np.array([20,21,20.5,20.8])
plt.figure(figsize=[4,5],dpi = 100)
plt.plot(x,y,color = 'red',marker = 'o')
plt.xlabel('big numbers',fontsize = 14)
plt.ylabel('small numbers',fontsize = 14)
plt.xlim(0,5)
plt.ylim(20,30)

y_error = np.array([0.12,0.13,0.2,0.1])
if(y_error == [0.12,0.13,0.2,0.1]):
    plt.errorbar(x,y_error)


import random
m = list(random.sample(range(51), 50))
n = list(random.sample(range(51), 50))
p = np.array(m)
q = np.array(n)
plt.scatter(m,n)
scratch = {'first_name': pd.Series(['Jason', 'Molly', 'Tina', 'Jake', 'Amy']),'last_name': pd.Series(['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze']), 'female': pd.Series([0, 1, 1, 0, 1]),'age': pd.Series([42, 52, 36, 24, 73]), 'preTestScore': pd.Series([4, 24, 31, 2, 3]),'postTestScore': pd.Series([25, 94, 57, 62, 70])}
scratchdf = pd.DataFrame(scratch)