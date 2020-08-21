import pandas as pd 
import numpy as np 

read = pd.read_csv('Salaries.csv')
df = pd.DataFrame(read)

#finding the increse in Totalpay from 2011 to 2014
df11 = df[df['Year']==2011]
df14 = df[df['Year']==2014]
avgpay11 = np.mean(df11['TotalPay'])
avgpay14 = np.mean(df14['TotalPay'])

print("pa increased from 2011 to 2014 avg : ",avgpay14-avgpay11)

#job title with the highest mean salary in 2014 
max14 = np.max(df14['TotalPay'])
(df14[df14['TotalPay'] == max14])['JobTitle']

# how much money is saved when overtime pay is stopped
df14_no_ot = df14[df14['OvertimePay'] == 0 ]
mean_pay_no_ot = np.mean(df14_no_ot['TotalPay'])
df14_yes_ot = df14[df14['OvertimePay']> 0 ]
mean_pay_yes_ot = np.mean(df14_yes_ot['TotalPay'])
savedmoney = (mean_pay_yes_ot-mean_pay_no_ot)
print("amount saved by not paying on overtime : " ,savedmoney)

# most common jobs 
l = df14['JobTitle'].value_counts()

dftransit = df14[df14['JobTitle']== 'Transit Operator']
dfsn = df14[df14['JobTitle']== 'Special Nurse']
dfrn = df14[df14['JobTitle']== 'Registered Nurse']
dfpsa = df14[df14['JobTitle']== 'Public Svc Aide-Public Works']
dffire = df14[df14['JobTitle']== 'Firefighter']
transitsum = np.sum(dftransit['TotalPay'])
specialnuresesum = np.sum(dfsn['TotalPay'])
registered_nurse_sum = np.sum(dfrn['TotalPay'])
public_svc_sum = np.sum(dfpsa['TotalPay'])
fire_sum = np.sum(dffire['TotalPay'])
sfo_sum = fire_sum + public_svc_sum + registered_nurse_sum + specialnuresesum + transitsum
print("the cost SFO needs to pay is : ",sfo_sum)
#max paid 
high = np.max(df['TotalPay'])
(df[df['TotalPay'] == high])['JobTitle']