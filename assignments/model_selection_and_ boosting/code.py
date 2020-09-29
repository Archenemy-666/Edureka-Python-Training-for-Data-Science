import pandas as pd 
from sklearn import model_selection 
from sklearn.ensemble import AdaBoostClassifier
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv('bio-degradable-data.csv',sep= ';',header=None)
df.columns = ['1','2','3','4','5','6','7',8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42]
array = df.values
x = array[: ,0:41]
y = array[: ,41]
kfold = model_selection.KFold(n_splits=10, random_state=7)
model = AdaBoostClassifier(n_estimators=30, random_state=7)
results = model_selection.cross_val_score(model, x, y, cv=kfold)
print(results.mean())