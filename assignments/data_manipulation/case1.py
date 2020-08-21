import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

read  = pd.read_csv('HollywoodMovies.csv')
df_movies = pd.DataFrame(read)
story = (df_movies[df_movies['Story'] == 'Quest'])
print(story)
maximum = np.max(story['RottenTomatoes'])
print(maximum)
maximum2 = np.max(story['AudienceScore'])
print(maximum2)
df_movies.sort_values(['Budget'],ascending=False).groupby('Movie').head(5)

profit = np.array(df_movies['Profitability'])
rotten = np.array(df_movies['RottenTomatoes'])
plt.bar(rotten,profit)

test = {'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'], 
        'last_name': ['Miller', 'Jacobson', ".", 'Milner', 'Cooze'],
         'age': [42, 52, 36, 24, 73], 
         'preTestScore': [4, 24, 31, ".", "."],
         'postTestScore': ["25,000", "94,000", 57, 62, 70] }
df_test = pd.DataFrame(test)
df_test.to_csv('testcase1.csv',header=False)
example = pd.read_csv('testcase1.csv')
df_test.set_axis(['First name ', 'Last name', '0', '1', '2'], axis=1, inplace=False)
df_test.to_csv('example.csv')
df_bool = df_test.replace(to_replace='\w',value = 0,regex=True)
df_bool = df_bool.replace(to_replace='.',value = 1)
m = range(2,101)
df_bool = df_bool.replace(to_replace=m,value = 0)
df_bool.astype('bool')

exampleskip = pd.read_csv('testcase1.csv',skiprows=3)
exampleskipdf = pd.DataFrame(exampleskip)
exampleskipdf

exampleth = pd.read_csv('example.csv',thousands=r',')

page3 = pd.Series(['Amit', 'Bob', 'Kate', 'A', 'b', np.nan, 'Car', 'dog', 'cat'])
page3.str.lower()
page3.str.upper()
page3.str.len()

page3_2 = pd.Series([' Atul', 'John ', ' jack ', 'Sam'])
page3_2.str.strip()
page3_2.str.lstrip()
page3_2.str.rstrip()

page3_3 = pd.Series(['India_is_big', 'Population_is_huge', np.nan, 'Has_diverse_culture'])
list1 = []
list1= page3_3.str.split('_')
list2 = []
i = range(0,4)
for line in list1[0]:
        list2.append(line)
list2
for line2 in list1[1]:
        list2.append(line2)
list2
for line3 in list1[3]:
        list2.append(line3)
print(list2)

page3_4 = pd.Series(['A', 'B', 'C', 'AabX', 'BacX','', np.nan, 'CABA', 'dog', 'cat'])
page3_5=page3_4.replace(to_replace='dog', value='XX-XX',regex=True)
page3_6 = page3_4.replace(to_replace='X',value = 'XX-XX',regex = True)

page3_7 = pd.Series(['12', '-$10', '$10,000'])

page3_7.replace('$','')

page3_8 = pd.Series(['india 1998', 'big country', np.nan])
page3_8[::-1]

page4 = pd.Series(['1', '2', '1a', '2b', '2003c'])
page4.str.isalnum()

page5 = pd.Series(['1', '2', '1a', '2b', 'America', 'VietnAm','vietnam', '2003c'])
page5.str.contains('A')

page5_1 = pd.Series(['a', 'a|b', np.nan, 'a|c'])

page5_2 = {'key': ['One', 'Two'], 'ltable': [1, 2]}
page5_21 = {'key': ['One', 'Two'], 'rtable': [4, 5]}
df5_2= pd.DataFrame(page5_2)
df5_21 = pd.DataFrame(page5_21)
df5_2.merge(df5_21,on= 'key')
