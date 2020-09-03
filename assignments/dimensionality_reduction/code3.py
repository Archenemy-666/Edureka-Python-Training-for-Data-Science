import pandas as pd
from  sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn import metrics

read = pd.read_csv('breast-cancer-data.csv')
df = pd.DataFrame(read)

le = LabelEncoder() 

target = le.fit_transform(df['diagnosis'])
features = df.iloc[: ,2:]

lda = LinearDiscriminantAnalysis(n_components= 1)
features_lda = lda.fit(features,target).transform(features)
print("Original number of features:", features.shape[1])
print("Reduced number of features:", features_lda.shape[1])


from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(features_lda, target, test_size=0.20, random_state=0)

logisticRegr = LogisticRegression()
logisticRegr.fit(x_train, y_train)
predictions = logisticRegr.predict(x_test)
print(metrics.accuracy_score(predictions,y_test))
print(metrics.confusion_matrix(predictions,y_test))

