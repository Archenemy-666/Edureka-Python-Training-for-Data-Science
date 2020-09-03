import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.datasets import load_digits
import matplotlib.pyplot as plt 
from sklearn.linear_model import LogisticRegression
from sklearn import metrics



digits = load_digits()

plt.gray() 
plt.matshow(digits.images[0]) 
plt.show() 

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size=0.20, random_state=0)
logisticRegr = LogisticRegression()
logisticRegr.fit(x_train, y_train)
predictions = logisticRegr.predict(x_test)
print(metrics.accuracy_score(predictions,y_test))
print(metrics.confusion_matrix(predictions,y_test))




features = StandardScaler().fit_transform(digits.data)
#retains 99 % of tthe varience
pca = PCA(n_components= 0.95 , whiten=True)
features_pca = pca.fit(features)
print("Original number of features: ",features.shape[1])
print("Reduced number of features: ",features_pca.shape[1])

x_train, x_test, y_train, y_test = train_test_split(features_pca, digits.target, test_size=0.25, random_state=0)
logisticRegr = LogisticRegression()
logisticRegr.fit(x_train, y_train)
predictions = logisticRegr.predict(x_test)
print(metrics.accuracy_score(predictions,y_test))
print(metrics.confusion_matrix(predictions,y_test))