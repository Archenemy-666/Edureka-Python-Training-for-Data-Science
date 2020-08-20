import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 

read = pd.read_csv('BigMartSalesData.csv')
df = pd.DataFrame(read)

year2011 = (df[df['Year']==2011])
month = np.array(year2011['Month'])
amount = np.array(year2011['Amount'])
country = np.array(year2011['Country'])
x = plt.plot(month,amount)
plt.pie(amount, labels = country)
month8 = (year2011[year2011['Month'] == 8]) 
np.mean(month8['Amount'])
x = np.min(month8['Amount'])
print(year2011[year2011['Amount'] == x])

