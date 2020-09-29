import pandas as pd 
import numpy as np 
from scipy.cluster.hierarchy import dendrogram,linkage
from sklearn.cluster import KMeans
import matplotlib.pyplot as  plt
import seaborn as sns

plt.rcParams['figure.figsize'] = (5,5)
plt.style.use('ggplot')

    
read = pd.read_csv('driver-data.csv')
df = pd.DataFrame(read)

#kmeans

kmeans = KMeans(n_clusters= 5)
kmeans.fit_transform(df)
kmeans.cluster_centers_
print(kmeans.labels_)
print(len(kmeans.labels_))
unique,counts = np.unique(kmeans.labels_,return_counts=True)
print(dict(zip(unique,counts)))


df['cluster'] = kmeans.labels_
sns.set_style('whitegrid')
sns.lmplot('self_reference_max_shares', 'mean_over_speed_perc',data=df, hue='cluster', palette='coolwarm',size=6,aspect=1,fit_reg=False)





