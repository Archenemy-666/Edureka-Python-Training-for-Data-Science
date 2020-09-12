import pandas as pd 
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder
read = pd.read_csv('run_or_walk.csv')
df = pd.DataFrame(read)



target = df['activity']
feature = df[['wrist','acceleration_x','acceleration_y','acceleration_z','gyro_x','gyro_y','gyro_z']]

feature2 = df[['acceleration_x','acceleration_y','acceleration_z']]
feature3 = df[['gyro_x','gyro_y','gyro_z']]
le = LabelEncoder()
user = le.fit_transform(df['username'])
df['username'] = user
gnb = GaussianNB()
gnb.fit(feature,target)
gnb.score(feature,target)

#only accelerated values as predictors 
gnb.fit(feature2,target)
gnb.score(feature2,target)

#only gyro values as predictors
gnb.fit(feature3,target)
gnb.score(feature3,target)