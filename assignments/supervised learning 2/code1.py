import pandas as pd 
from sklearn.svm import SVC

read = pd.read_csv('voice-classification.csv')
df = pd.DataFrame(read)

features = df.iloc[: ,0:20]
target = df['label']

svc = SVC(C=1,gamma='auto')
model = svc.fit(features,target)
model.support_vectors_

svc.predict(features)
svc.score(features,target)