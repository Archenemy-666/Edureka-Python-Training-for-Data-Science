import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.preprocessing import LabelEncoder

data = pd.read_csv('horse.csv')
df = pd.DataFrame(data)

#checking for null values 
df['surgery'].describe()
df['surgery'] = df['surgery'].fillna(value = 'Yes')
df['age'].describe()
df['age'] = df['age'].fillna(value = 'adult')
df['temp_of_extremities'].describe()
df['temp_of_extremities'] = df['temp_of_extremities'].fillna(value = 'cool')
df['peripheral_pulse'].describe()
df['peripheral_pulse'] = df['peripheral_pulse'].fillna(value = 'normal')
df['mucous_membrane'].describe()
df['mucous_membrane'] = df['mucous_membrane'].fillna(value = 'normal_pink')

df['capillary_refill_time'].describe()
df['capillary_refill_time'] = df['capillary_refill_time'].fillna(value = 'less_3_sec')
df['capillary_refill_time'] = df['capillary_refill_time'].replace(to_replace=3,value = 'less_3_sec',regex=True)

df['pain'].describe()
df['pain'] = df['pain'].fillna(value = 'mild_pain')
df["peristalsis"].describe()
df['peristalsis'] = df['peristalsis'].fillna(value = 'hypomotile')
# its tough to decide when proper data isnt provided
df["abdominal_distention"].value_counts()
df['abdominal_distention'] = df['abdominal_distention'].fillna(value = 'moderate')

df["nasogastric_tube"].describe()
df['nasogastric_tube'] = df['nasogastric_tube'].fillna(value = 'slight')
df["nasogastric_reflux"].value_counts()
df['nasogastric_reflux'] = df['nasogastric_reflux'].fillna(value = 'more_1_liter')
df["rectal_exam_feces"].describe()
df['rectal_exam_feces'] = df['rectal_exam_feces'].fillna(value = 'absent')
df["abdomen"].describe()
df['abdomen'] = df['abdomen'].fillna(value = 'distend_large')
df["abdomo_appearance"].describe()
df['abdomo_appearance'] = df['abdomo_appearance'].fillna(value = 'cloudy')
df["outcome"].describe()
df['outcome'] = df['outcome'].fillna(value = 'lived')
df["surgical_lesion"].describe()
df['surgical_lesion'] = df['surgical_lesion'].fillna(value = 'yes')
df['cp_data'].describe()
df['cp_data'] = df['cp_data'].fillna(value = 'no')

#encoding categorical values 

le = LabelEncoder()
surgery1 = le.fit_transform(df['surgery'])
age1 = le.fit_transform(df['age'])
temp_of_extremities1 = le.fit_transform(df['temp_of_extremities'])
peripheral_pulse1 = le.fit_transform(df['peripheral_pulse'])
mucous_membreane1 = le.fit_transform(df['mucous_membrane'])
capillary_refill_time1 = le.fit_transform(df['capillary_refill_time'])
pain1 = le.fit_transform(df['pain'])
peristalsis1 = le.fit_transform(df["peristalsis"])
abdominal_distention1 = le.fit_transform(df["abdominal_distention"])
nasogastric_tube1 = le.fit_transform(df["nasogastric_tube"])
nasogastric_reflux1 = le.fit_transform(df["nasogastric_reflux"])
rectal_exam_feces1 = le.fit_transform(df["rectal_exam_feces"])
abdomen1 = le.fit_transform(df["abdomen"])
abdomo_appearance1 =le.fit_transform(df["abdomo_appearance"])
outcome1 = le.fit_transform(df["outcome"])
surgical_lesion1 = le.fit_transform(df["surgical_lesion"])
cp_data1 = le.fit_transform(df['cp_data'])

#replacing categorical values with encoded values

df['surgery'] =  surgery1
df['age'] = age1
df['temp_of_extremities'] = temp_of_extremities1
df['peripheral_pulse'] = peripheral_pulse1
df['mucous_membrane'] = mucous_membreane1
df['capillary_refill_time'] = capillary_refill_time1
df['pain'] = pain1
df["peristalsis"] = peristalsis1
df["abdominal_distention"] = abdominal_distention1
df["nasogastric_tube"] = nasogastric_tube1
df["nasogastric_reflux"] = nasogastric_reflux1
df["rectal_exam_feces"] = rectal_exam_feces1
df["abdomen"] = abdomen1
df["abdomo_appearance"] = abdomo_appearance1 
df["outcome"] = outcome1
df["surgical_lesion"] = surgical_lesion1
df['cp_data'] = cp_data1



#decision tree 

train,test = train_test_split(df,test_size = 0.3 )
print(train.shape)
print(test.shape)
predict = ["surgery","age","rectal_temp","pulse","respiratory_rate","temp_of_extremities","peripheral_pulse","mucous_membrane","capillary_refill_time","pain","peristalsis","abdominal_distention","nasogastric_tube","nasogastric_reflux","nasogastric_reflux_ph","rectal_exam_feces","abdomen","packed_cell_volume","total_protein","abdomo_appearance","abdomo_protein","outcome","surgical_lesion","lesion_1","lesion_2","lesion_3"]
train_x = train[predict]
train_y = train['cp_data']
train_x = train_x.fillna(value = 0 )

test_x = test[predict]
test_y = test['cp_data']
test_x = test_x.fillna(value = 0 )

model = tree.DecisionTreeClassifier()
model.fit(train_x,train_y)

prediction = model.predict(test_x)

print(metrics.accuracy_score(prediction,test_y))