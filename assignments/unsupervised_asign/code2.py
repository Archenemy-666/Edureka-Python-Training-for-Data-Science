from PIL import Image
import pandas as pd
import numpy as np
from numpy import asarray
import math 
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans



image = Image.open('dogs.jpeg')
image.size



data = asarray(image)
data.shape

math.sqrt(150960)
image_2d = np.reshape(data,(75480,2))
df = pd.DataFrame(image_2d)
df['one'] = df.iloc[: , 0]
df['two'] = df.iloc[: , 1]

kmeans = KMeans(n_clusters= 3)

kmeans.fit(df)
kmeans.cluster_centers_
print(len(kmeans.labels_))
unique , count = np.unique(kmeans.labels_,return_counts=True)
print(dict(zip(unique , count)))

df['cluster'] = kmeans.labels_
sns.set_style('whitegrid')
sns.lmplot('one','two',data=df, hue='cluster', palette='coolwarm',size=6,aspect=1,fit_reg=False)


