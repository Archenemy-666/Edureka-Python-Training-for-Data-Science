import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import numpy as np
from scipy.spatial.distance import cdist
from  sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram,linkage
import seaborn as sns
from sklearn.metrics import mean_squared_error


read = pd.read_csv('Project_Data_1.csv')
read.values
read1 = read.iloc[: , 1:]
df = pd.DataFrame(read)
#checking for empty values 
df
df.isnull()
#renaming header 
df = df.rename(columns={'Sales of Wheat in tons':'Country'})

df['Country'].dropna()
df_no_country = df.iloc[: ,1:]
df_no_country
# convert he string values to float
df = df[df['1990'].str.isnumeric()]
df = df[df['1991'].str.isnumeric()]
df = df[df['1992'].str.isnumeric()]
df = df[df['1993'].str.isnumeric()]
df = df[df['1994'].str.isnumeric()]
df = df[df['1995'].str.isnumeric()]
df = df[df['2005'].str.isnumeric()]
df = df[df['2006'].str.isnumeric()]
df = df[df['2007'].str.isnumeric()]

#label encoding the countries  
le = LabelEncoder()
df['Country'] = le.fit_transform(df['Country'])
df['Country']
df

#applying PCA
pca = PCA(n_components= 0.95 , whiten=True)
features_pca = pca.fit_transform(df)
print("Original number of features: ",df.shape[1])
print("Reduced number of features: ",features_pca.shape[1])




#kmeans
distortions = [] 
inertias = [] 
mapping1 = {} 
mapping2 = {} 
K = range(1,10) 
  
for k in K: 
    #Building and fitting the model 
    kmeanModel = KMeans(n_clusters=k).fit(df) 
    kmeanModel.fit(df)     
      
    distortions.append(sum(np.min(cdist(df, kmeanModel.cluster_centers_, 
                      'euclidean'),axis=1)) / df.shape[0]) 
    inertias.append(kmeanModel.inertia_) 
  
    mapping1[k] = sum(np.min(cdist(df, kmeanModel.cluster_centers_, 
                 'euclidean'),axis=1)) / df.shape[0] 
    mapping2[k] = kmeanModel.inertia_ 


#Using the different values of distortion

for key,val in mapping1.items(): 
    print(str(key)+' : '+str(val)) 


plt.plot(K, distortions, 'bx-') 
plt.xlabel('Values of K') 
plt.ylabel('Distortion') 
plt.title('The Elbow Method using Distortion') 
plt.show() 

for key,val in mapping2.items(): 
    print(str(key)+' : '+str(val))


#Using the different values of Inertia
plt.plot(K, inertias, 'bx-') 
plt.xlabel('Values of K') 
plt.ylabel('Inertia') 
plt.title('The Elbow Method using Inertia') 
plt.show()



#spliting to train and test 
df['mean'] = df.mean(axis = 1)

features = ['mean']
train,test = train_test_split(df,test_size = 0.20)
train_x = train[features]
train_y = train['Country']

test_x = test[features]
test_y = test['Country']

#agglomerative clustering
den = dendrogram(linkage(df,method = 'ward'))

model = AgglomerativeClustering(n_clusters=2, affinity='euclidean', linkage='ward')
model.fit(train_x,train_y)
predict = model.fit_predict(test_x)
mean_squared_error(test_y,predict)
labels = model.labels_

#kmeans



kmeans = KMeans(n_clusters= 2)

kmeans.fit(df)
kmeans.cluster_centers_
print(len(kmeans.labels_))
unique , count = np.unique(kmeans.labels_,return_counts=True)
print(dict(zip(unique , count)))

df['cluster'] = kmeans.labels_
sns.set_style('whitegrid')
sns.lmplot('Country','mean',data=df, hue='cluster', palette='coolwarm',size=6,aspect=1,fit_reg=False)