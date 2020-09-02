import pandas as pd 
import numpy as np 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
read = pd.read_csv('loan_borowwer_data.csv')
df = pd.DataFrame(read)

#data wrangling 
le = LabelEncoder()
df['purpose'] = le.fit_transform(df['purpose'])
df['credit.policy'].unique
corr = df.corr()
sns.heatmap(corr)
df['purpose']

# logistic regression 
prediction = ['credit.policy','purpose','int.rate', 'installment','log.annual.inc','dti','fico','days.with.cr.line','revol.bal','revol.util','inq.last.6mths','delinq.2yrs','pub.rec']

train,test = train_test_split(df,test_size = 0.3)
train_x = train[prediction]
train_y = train['not.fully.paid']

test_x = test[prediction]
test_y = test['not.fully.paid']

lg = LogisticRegression()
lg.fit(train_x,train_y)
pred = lg.predict(test_x)
print(metrics.accuracy_score(pred,test_y))
