import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

read = pd.read_csv('prisoners.csv')
df = pd.DataFrame(read)
df.head()
df.describe()
# looking into rows with zero inmates 
zeroed = df.loc[df['No. of Inmates benefitted by Elementary Education'] == 0]
zeroed.describe()
# we can conclude that chandigarh and mizoram are exception
# sum ofonmates benefitted
benefited = df.sum()
benrow = df.append(benefited,ignore_index='YEAR')
#added column who benefitted in prison from different states
df['benefited'] = df.drop('YEAR', axis=1).sum(axis=1)

state = np.array(df['STATE/UT'])
beni = np.array(df['benefited'])
plot1 = plt.bar(state,beni)
max2 = np.max(beni)
df[df['benefited'] == max2]
plt.pie(beni,labels=state)