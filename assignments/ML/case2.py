import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns

read = pd.read_csv('cereal.csv')
df = pd.DataFrame(read)
sugars = np.array(df['sugars'])
vitamins = np.array(df['vitamins'])
plt.hist(sugars)
plt.hist(vitamins)

# add a new column with full names 
df1 = df['mfr'].replace(to_replace=('N','Q','K','R','G','P','A'),value =  ('Nabisco','Quaker Oats','Kelloggs','Raslston Purina','General Mills' ,'Post' ,'American Home Foods Products'))
mfr = np.array(df1)
df['full_names_mfr'] = mfr

(df['full_names_mfr'].value_counts().plot(kind = 'bar',figsize = (14,8)))

# starting ML
correlation = df.corr()
sns.heatmap(correlation,square=True)
plt.yticks(rotation = 0)
plt.xticks(rotation = 90)
plt.show()

x = df.iloc[:,3:14]
y = df["rating"]

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.25,random_state = 5)
x_train.head()

from sklearn.linear_model import LinearRegression
lr = LinearRegression()
model = lr.fit(x_train,y_train)

pred_y = lr.predict(x_test)

plt.scatter(y_test,y_test.index,color = 'r')
plt.scatter(pred_y,y_test.index,color = 'b')

plt.xlabel('Y Test')
plt.ylabel('Predicted Y')