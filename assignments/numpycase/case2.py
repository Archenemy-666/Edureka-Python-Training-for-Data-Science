import pandas as pd 
import numpy as np 

read_p = pd.read_csv('PhysicsScoreTerm1.csv')
read_m = pd.read_csv('MathScoreTerm1.csv')
read_d = pd.read_csv('DSScoreTerm1.csv')

physics = pd.DataFrame(read_p)
math = pd.DataFrame(read_m)
ds = pd.DataFrame(read_d)

mergeing1 = pd.merge(math,physics,on = 'ID')
mergingfinal = pd.merge(mergeing1,ds,on = 'ID')
mergingfinal = mergingfinal.replace(regex = 'White American',value = 'W')
mergingfinal = mergingfinal.replace(regex = 'European American',value = 'E')
mergingfinal = mergingfinal.replace(regex = 'Hispanic',value = 'H')
mergingfinal = mergingfinal.replace(regex = 'African American',value = 'A')
mergingfinal.Ethinicity_x.unique()

up = physics.drop(columns = ['Name','Ethinicity'])
um = math.drop(columns = ['Name','Ethinicity'])
ud = ds.drop(columns = ['Name','Ethinicity'])
meanup = np.mean(up["Score"])
meanum = np.mean(um["Score"])
meands = np.mean(ds["Score"])
up.fillna(meanup,inplace = True)
um.fillna(meanum,inplace = True)
ud.fillna(meands,inplace = True)

subfinal=(pd.merge(up,ud,on = 'ID'))
final = (pd.merge(subfinal,um,on = 'ID'))
print(final)

final = final.replace(regex='M', value=1)
final = final.replace(regex = 'F',value = 2)

final.to_csv('newsource.csv')