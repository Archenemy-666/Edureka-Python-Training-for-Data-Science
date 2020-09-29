import requests, pandas as pd, numpy as np
from pandas import DataFrame
from io import StringIO
import time, json
from datetime import date
from statsmodels.tsa.stattools import adfuller, acf, pacf
from statsmodels.tsa.arima_model import ARIMA
from statsmodels.tsa.seasonal import seasonal_decompose
from sklearn.metrics import mean_squared_error
import matplotlib.pylab as plt
from matplotlib.pylab import rcParams
rcParams['figure.figsize'] = 15, 6
#reading the file 
df_fx_data = pd.read_csv('SeaPlaneTravel.csv')
#converting int values in csv to type datetime 
df_fx_data['Month'] = pd.to_datetime(df_fx_data['Month'])
#indexing file to dates 
indexed_df = df_fx_data.set_index('Month')
tf = indexed_df['#Passengers']
plt.plot(tf_month)

#printing vales of  the dataframe accourding to monthly basis 

tf_month  = tf.resample('M').mean()
plt.plot(tf_month)

#checking whether the data is stationary 

def check_stationarity(time_series):
    #determining rolling mean statistics 
    rolmean = time_series.rolling(window = 25 , center = False).mean()
    rolstd = time_series.rolling(window = 25, center = False).std()

    # plot rolling stats 

    orig = plt.plot(time_series , color = 'green', label = 'original')
    mean = plt.plot(rolmean, color = 'blue' , label =  'mean')
    std = plt.plot(rolstd , color = 'red', label = 'standard_deviation')
    plt.legend('best')
    plt.title('Rolling mean and the Rolling Standard Deviation ')

    #performing Dickey fuller Test 

    print("performing dickey Fuller test")
    df_test = adfuller(time_series,autolag = 'AIC')
    df_output = pd.Series(df_test[0:4],index=['Test Statistic','p-value','#Lags Used','Number of Observations Used'])

    for key, value in df_test[4].items():
        df_output['critical value (%s)'%key] = value 
    print(df_output) 
check_stationarity(tf)
# p value is greater than 0.05 hence its not stationary 
# applying differencing to stationary data . 
tf_log = np.log(tf)
tf_log_diff = tf_log - tf_log.shift()
plt.plot(tf_log_diff)
tf_log_diff.dropna(inplace = True)
check_stationarity(tf_log_diff)

#test statistic less than 1 % critical value
#defining acf and pacf

lag_acf = acf(tf_log_diff,nlags = 5)
lag_pacf = pacf(tf_log_diff,nlags = 5 , method='ols')

#ploting acf 
plt.subplot(121) 
plt.plot(lag_acf)
plt.axhline(y=0,linestyle='--',color='gray')
plt.axhline(y=-2/np.sqrt(len(tf_log_diff)),linestyle='--',color='gray')
plt.axhline(y=2/np.sqrt(len(tf_log_diff)),linestyle='--',color='gray')
plt.title('Autocorrelation Function')

#ploting pacf
plt.subplot(122)
plt.plot(lag_pacf)
plt.axhline(y=0,linestyle='--',color='gray')
plt.axhline(y=-2/np.sqrt(len(tf_log_diff)),linestyle='--',color='gray')
plt.axhline(y=2/np.sqrt(len(tf_log_diff)),linestyle='--',color='gray')
plt.title('Partial Autocorrelation Function')
plt.tight_layout()

#ARIMA ( p = 2 , q = 1 no.of differencing d = 1)

model = ARIMA(tf_log, order=(2, 1, 1))  
results_ARIMA = model.fit(disp=-1)  
plt.plot(tf_log_diff)
plt.plot(results_ARIMA.fittedvalues, color='red')
plt.title('RSS: %.4f'% sum((results_ARIMA.fittedvalues-tf_log_diff)**2))

#analysis
print(results_ARIMA.summary())
# residual errors
residuals = DataFrame(results_ARIMA.resid)
residuals.plot(kind='kde')
print(residuals.describe())

predictions_ARIMA_diff = pd.Series(results_ARIMA.fittedvalues, copy=True)
print (predictions_ARIMA_diff.head())

predictions_ARIMA_diff_cumsum = predictions_ARIMA_diff.cumsum()
predictions_ARIMA_log = pd.Series(tf_log.iloc[0], index=tf_log.index)
predictions_ARIMA_log = predictions_ARIMA_log.add(predictions_ARIMA_diff_cumsum,fill_value=0)
predictions_ARIMA = np.exp(predictions_ARIMA_log)
plt.plot(tf)
plt.plot(predictions_ARIMA)
plt.title('RMSE: %.4f'% np.sqrt(sum((predictions_ARIMA-tf)**2)/len(tf)))

size = int(len(tf_log) - 15)
train, test = tf_log[0:size], tf_log[size:len(tf_log)]
history = [x for x in train]
predictions = list()

size = int(len(tf_log) - 15)
train, test = tf_log[0:size], tf_log[size:len(tf_log)]
history = [x for x in train]
predictions = list()
print('Printing Predicted vs Expected Values...')
print('\n')
for t in range(len(test)):
    model = ARIMA(history, order=(2,1,1))
    model_fit = model.fit(disp=0)
    output = model_fit.forecast()
    yhat = output[0]
    predictions.append(float(yhat))
    obs = test[t]
    history.append(obs)
print('predicted=%f, expected=%f' % (np.exp(yhat), np.exp(obs)))

error = mean_squared_error(test, predictions)
print('\n')
print('Printing Mean Squared Error of Predictions...')
print('Test MSE: %.6f' % error)
predictions_series = pd.Series(predictions, index = test.index)

fig, ax = plt.subplots()
ax.set(title='time passengers ', xlabel='Date', ylabel='passengers')
ax.plot(tf[-60:], 'o', label='observed')
ax.plot(np.exp(predictions_series), 'g', label='rolling one-step out-of-sample forecast')
legend = ax.legend(loc='upper left')
legend.get_frame().set_facecolor('w')