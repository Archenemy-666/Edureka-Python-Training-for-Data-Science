
#Classification for Online News Popularity
#Importing the Libraries
import pandas as pd
from sklearn.cluster import KMeans
import seaborn as sns
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import confusion_matrix
#Importing the dataset
dataset = pd.read_csv('OnlineNewsPopularity.csv')
df = pd.DataFrame(dataset)

data = df.iloc[:,2:]

'''
kmeans = KMeans(n_clusters = 3)
kmeans.fit_transform(data)
kmeans.cluster_centers_
kmeans.labels_
unique,counts = np.unique(kmeans.labels_,return_counts=True)
print(dict(zip(unique,counts)))
data['cluster'] = kmeans.labels_
sns.set_style('whitegrid')
sns.lmplot('n_tokens_title', 'shares',data=data, hue='cluster',palette='coolwarm',size=6,aspect=1,fit_reg=False)

'''





features = dataset.iloc[:,2:-2].values
output = dataset.iloc[:, -1].values
#Training set and Test set
x_train, x_test, y_train, y_test = train_test_split(features, output, test_size = 0.2, random_state = 0)
#Gradient Boosting to Training set
gbc = GradientBoostingClassifier()
gbc.fit(x_train, y_train)
y_pred = gbc.predict(x_test)

cm = confusion_matrix(y_test, y_pred)
