import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics

read = pd.read_csv('voice.csv')
df = pd.DataFrame(read)
enc = OneHotEncoder(handle_unknown='ignore')
df_bin = pd.DataFrame(enc.fit_transform(df[['label']]).toarray())
df = df.join(df_bin)

# data wranging 
df.drop("label",axis = 1,inplace=True)
df = df.rename({0:'labelled1'},axis=1)
df = df.rename({1:'labelled2'},axis=1)
df
corr = df.corr()
corr
sns.heatmap(corr)
# splitting columns to train 
prediction_var = ["meanfreq","sd","median","Q25","Q75","IQR","skew","kurt","sp.ent","sfm","mode","centroid","meanfun","minfun","maxfun","meandom","mindom","maxdom","dfrange","modindx"]
dep = ['labelled1','labelled2']
#traintest 
train,test = train_test_split(df,test_size = 0.3)
print(train.shape)
print(test.shape)
train_x = train[prediction_var]
train_y = train['labelled1']

test_x = test[prediction_var]
test_y = test['labelled1']

logistic = LogisticRegression()
logistic.fit(train_x,train_y)
temp = logistic.predict(test_x)
print(metrics.accuracy_score(temp,test_y))

