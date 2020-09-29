import pandas as pd 
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

read2 = pd.read_csv('BX-Books.csv',encoding = 'ISO-8859-1')
read1 = pd.read_csv('BX-Book-Ratings.csv',encoding = 'ISO-8859-1')
read3 = pd.read_csv('BX-Users.csv',encoding = 'ISO-8859-1')

df1 = pd.DataFrame(read1)
df2 = pd.DataFrame(read2)
df3 = pd.DataFrame(read3)


dfs = pd.merge(df3 , df1 , on = 'user_id')
df = pd.merge(dfs,df2,on = 'isbn')
#basket = df.groupby(['user_id','book_author'])['rating'].sum().reset_index().fillna(0).set_index('user_id')
l = df.head(1000)
l.fillna(0)
basket = l.pivot(index = 'user_id',columns = 'publisher',values = 'rating')
basket = basket.fillna(0)
basket
def encode_units(x):
    if x <= 0:
        return 0
    if x >= 1:
        return 1
basket_sets = basket.applymap(encode_units)
basket_sets

frequent_itemsets = apriori(basket_sets, min_support=0.07, use_colnames=True)
rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)
rules.head()
