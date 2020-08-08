import os 
import pandas as pd
import numpy as np
from scipy import stats

x = pd.read_csv('bank-data.csv')
df = pd.DataFrame(x)
type(df)
print(df)
df.to_csv('bank-data.csv',index=False,sep = ',')
df_csv = pd.read_csv('bank-data.csv',header=0,sep=',')
help(df_csv)
df_csv.ndim
df_csv["job"]

for i in df_csv["job"]:
    print(i)

job_count = df_csv.pivot_table(index=['job'], aggfunc='size')
print(job_count)

print(max(job_count))
print(min(job_count))
mean = np.mean(job_count)
mode = stats.mode(job_count)
print(mode)

unique_jobs = dict(job_count)
print(unique_jobs)

accepted = []
accepted = unique_jobs.keys()
loan = (job_count >= mean)
print(loan)
loan_df = pd.DataFrame(loan)
type(loan_df)
print(loan_df)
loan_df
print(loan_df)
please = dict(loan_df)
type(please)
people = input("enter profession : ")
if people in please : 
    if please == True :
        print("ok")
