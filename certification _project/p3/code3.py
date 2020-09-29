
#       LIBRARIES
import pandas as pd 
import numpy as np 
from sklearn.preprocessing import LabelEncoder 
from sklearn.metrics import accuracy_score
#plot libraries
import matplotlib.pyplot as pyplot
import seaborn as sns

#Machine learning libraries
from sklearn.model_selection import train_test_split

#       CODE 

# reading files 
test1 = pd.read_csv('test.csv')
train1 = pd.read_csv('train.csv')

df_test = pd.DataFrame(test1)
df_train = pd.DataFrame(train1)

#label encoding
le = LabelEncoder()
df_train['species'] = le.fit_transform(df_train['species'])

#dataset spliting

train , test = train_test_split(df_train,test_size = 0.20) 
features = ['margin1','margin2','margin3','margin4','margin5','margin6','margin7','margin8','margin9','margin10','margin11','margin12','margin13','margin14','margin15','margin16','margin17','margin18','margin19','margin20','margin21','margin22','margin23','margin24','margin25','margin26','margin27','margin28','margin29','margin30','margin31','margin32','margin33','margin34','margin35','margin36','margin37','margin38','margin39','margin40','margin41','margin42','margin43','margin44','margin45','margin46','margin47','margin48','margin49','margin50','margin51','margin52','margin53','margin54','margin55','margin56','margin57','margin58','margin59','margin60','margin61','margin62','margin63','margin64','shape1','shape2','shape3','shape4','shape5','shape6','shape7','shape8','shape9','shape10','shape11','shape12','shape13','shape14','shape15','shape16','shape17','shape18','shape19','shape20','shape21','shape22','shape23','shape24','shape25','shape26','shape27','shape28','shape29','shape30','shape31','shape32','shape33','shape34','shape35','shape36','shape37','shape38','shape39','shape40','shape41','shape42','shape43','shape44','shape45','shape46','shape47','shape48','shape49','shape50','shape51','shape52','shape53','shape54','shape55','shape56','shape57','shape58','shape59','shape60','shape61','shape62','shape63','shape64','texture1','texture2','texture3','texture4','texture5','texture6','texture7','texture8','texture9','texture10','texture11','texture12','texture13','texture14','texture15','texture16','texture17','texture18','texture19','texture20','texture21','texture22','texture23','texture24','texture25','texture26','texture27','texture28','texture29','texture30','texture31','texture32','texture33','texture34','texture35','texture36','texture37','texture38','texture39','texture40','texture41','texture42','texture43','texture44','texture45','texture46','texture47','texture48','texture49','texture50','texture51','texture52','texture53','texture54','texture55','texture56','texture57','texture58','texture59','texture60','texture61','texture62','texture63','texture64']

train_x = train[features]
train_y = train['species']

test_x = test[features]
test_y = test['species']

# Machine Learning models 
# SVM 



from sklearn.svm import SVC
svc = SVC(C = 1 , gamma = 'auto')
model_svc = svc.fit(train_x,train_y)
model_svc.support_vectors_

predict = svc.predict(test_x)
svc.score(train_x,train_y)
svc.score(test_x,test_y)

acc_of_SVM = accuracy_score(predict,test_y)
print("accuracy of SVM model",acc_of_SVM*100)

#NBGaussian

from sklearn.naive_bayes import GaussianNB
gnb = GaussianNB()
model_gnb = gnb.fit(train_x,train_y)
pred = gnb.predict(test_x)
acc_of_GNB = gnb.score(test_x,test_y)

print("accuracy of Naive abyes model",acc_of_GNB*100)


#Decision Tree Model 
from sklearn import tree 

dt = tree.DecisionTreeClassifier()
model_dt = dt.fit(train_x,train_y)
dt.predict(test_x)
acc_of_DT = dt.score(test_x,test_y)

print("accuracy of decision tree model",acc_of_DT*100)


#Random forest Model 
from sklearn.ensemble import RandomForestClassifier

rfc = RandomForestClassifier()
model_rfc = rfc.fit(train_x,train_y)
rfc.predict(test_x)
acc_of_rfc = rfc.score(test_x,test_y)
print("accuracy of random forest model",acc_of_rfc*100)
test_x.shape

# applying it on test.csv
rfc.predict(df_test.iloc[: , 1:])






