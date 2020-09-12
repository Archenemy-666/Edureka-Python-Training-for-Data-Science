import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.preprocessing import LabelEncoder
from  sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram,linkage
from  sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error



read = pd.read_csv('zoo.csv')
df = pd.DataFrame(read)
features = ['hair','feathers','eggs','milk','airborne','aquatic','predator','toothed','backbone','breathes','venomous','fins','legs','tail','domestic','catsize']
train,test = train_test_split(df,test_size = 0.20)
train_x = train[features]
train_y = train['class_type']

test_x = test[features]
test_y = test['class_type']



x = df.iloc[: , 1:].values





x = df.iloc[: , 1:].values
den = dendrogram(linkage(x,method = 'ward'))

model = AgglomerativeClustering(n_clusters=5, affinity='euclidean', linkage='ward')
model.fit(train_x,train_y)
predict = model.fit_predict(test_x)
mean_squared_error(test_y,predict)
labels = model.labels_