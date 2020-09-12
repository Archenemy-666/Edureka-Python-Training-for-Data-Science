import pandas as pd 
from sklearn.preprocessing import LabelEncoder , StandardScaler
from sklearn.svm import LinearSVC ,SVC
from sklearn.model_selection import train_test_split,GridSearchCV
from sklearn.metrics import confusion_matrix,classification_report


read = pd.read_csv('College.csv')
df = pd.DataFrame(read)

# target and features
features = df[["Apps","Accept","Enroll","Top10perc","Top25perc","F.Undergrad","P.Undergrad","Outstate","Room.Board","Books","Personal","PhD","Terminal","S.F.Ratio","perc.alumni","Expend","Grad.Rate"]]
target1 = df['Private']

#label encoding target 
le = LabelEncoder()
target = le.fit_transform(target1)
df['Private'] = target


#linear svc

svc = LinearSVC()
model = svc.fit(features,target)
model.predict(target)
model.score(features,target)


# standardizing features 
scaler = StandardScaler()
std_features = scaler.fit_transform(features)

#using standerdized feataures for svc to compare previous accuracy 

model2 = svc.fit(std_features,target)
model2.score(std_features,target)

feat = ["Apps","Accept","Enroll","Top10perc","Top25perc","F.Undergrad","P.Undergrad","Outstate","Room.Board","Books","Personal","PhD","Terminal","S.F.Ratio","perc.alumni","Expend","Grad.Rate"]
tar = ['Private']
train,test = train_test_split(df,test_size = 0.20)
train_x = train[feat]
train_y = train[tar]

test_x = test[feat]
test_y = test[tar]

svc1 = SVC()
svc1.fit(train_x,train_y)
pred = svc1.predict(test_x)
print(classification_report(test_y,pred))
#performing grid search 

param_grid = {'C': [0.1, 1, 10, 100, 1000],  
              'gamma': [1, 0.1, 0.01, 0.001, 0.0001], 
              'kernel': ['rbf']}  
  
grid = GridSearchCV(SVC(), param_grid, refit = True, verbose = 3) 
  
# fitting the model for grid search 
grid.fit(train_x, train_y) 

# print best parameter after tuning 
print(grid.best_params_) 
  
# print how our model looks after hyper-parameter tuning 
print(grid.best_estimator_)

grid_pred = grid.predict(test_x) 
  
# print classification report 
print(classification_report(test_y, grid_pred))