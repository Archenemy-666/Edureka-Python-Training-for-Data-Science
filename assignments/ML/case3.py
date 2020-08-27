import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from scipy import stats

read = pd.read_csv('FyntraCustomerData.csv')
df = pd.DataFrame(read)

correlation = df[['Time_on_Website','Yearly_Amount_Spent']].corr()
print(correlation)
sns.heatmap(correlation)
x = df['Time_on_Website']
y = df['Yearly_Amount_Spent']
z = df['Time_on_App']
a = df['Length_of_Membership']
g = sns.jointplot(x=x,y=y,kind='reg')    
h = sns.jointplot(x=z,y=y,kind='reg')
cor1 = np.corrcoef(x,y)
cor2 = np.corrcoef(y,z)
cor1coeff = cor1[0,1]**2
cor2coeff = cor2[0,1]**2

explore = sns.pairplot(df)
linearplot = sns.regplot(a,y)

x = df.iloc[:,3:7]


from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.25,random_state = 85)
x_train.head()

from sklearn.linear_model import LinearRegression
lr = LinearRegression()
model = lr.fit(x_train,y_train)

pred_y = lr.predict(x_test)

plt.scatter(y_test,y_test.index,color = 'r')
plt.scatter(pred_y,y_test.index,color = 'b')

plt.xlabel('Y Test')
plt.ylabel('Predicted Y')

