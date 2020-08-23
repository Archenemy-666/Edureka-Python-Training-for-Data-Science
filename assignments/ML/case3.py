import pandas as pd 
import numpy as np
import seaborn as sns 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
read = pd.read_csv('FyntraCustomerData.csv')
df = pd.DataFrame(read)

df[['Time_on_Website','Yearly_Amount_Spent']]