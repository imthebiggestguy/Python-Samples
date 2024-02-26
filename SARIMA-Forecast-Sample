#Sample SARIMA Forecast

import pandas as pd
import datetime as dt
import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.statespace.sarimax import SARIMAX
import numpy as np
from sklearn.metrics import mean_squared_error

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

#Input Parameters on date range and security we want to forecast
security = "SPY"
start = dt.datetime(2021, 1, 1)
end = dt.datetime(2023, 12, 31)

#Download data
data = yf.download(security, start, end)
data.to_csv("security.csv")

#Read data from the CSV file and set the 'Date' column as the index
data = pd.read_csv("security.csv", parse_dates=['Date'], index_col='Date')

#Data visualization library (seaborn) allows us to customize appearance
sns.set()

#Plot definitions
plt.ylabel('Security Price')
plt.xlabel('Date')
plt.xticks(rotation=45)
plt.title(f"SARIMA Forecast vs Actuals ${security} ")

#Train/Test split for Security Data
train = data[data.index <= pd.to_datetime("2023-6-01", format='%Y-%m-%d')]
test = data[data.index >= pd.to_datetime("2023-6-01", format='%Y-%m-%d')]

#SARIMA Forecast
y = train['Close']
SARIMAXmodel = SARIMAX(y, order = (4, 3, 2), season_order = (4, 2, 2, 12))
SARIMAXmodel = SARIMAXmodel.fit()
y_pred = SARIMAXmodel.get_forecast(len(test.index))

#alpha = 0.05, therefore 5% chance real value will be outside upper&lower bound -> 95% CI
forecast_SARIMAX = y_pred.conf_int(alpha = 0.05) 
forecast_SARIMAX["SARIMA Forecast"] = SARIMAXmodel.predict(start = forecast_SARIMAX.index[0], end = forecast_SARIMAX.index[-1])
forecast_SARIMAX.index = test.index

#predicted values of the SARIMA Model
SARIMAX_Var = forecast_SARIMAX["SARIMA Forecast"] 

#Plot for SARIMA Forecast, Training, Testing
plt.plot(SARIMAX_Var, color='red', label = 'SARIMA Forecast')
plt.plot(train['Close'], color="black", label='Training Range')
plt.plot(test['Close'], color="green", label='Testing Range')

#Show the plot
plt.legend()
plt.tight_layout()
plt.show()

#Returning the performance of RMSE
sarimax_rmse = np.sqrt(mean_squared_error(test['Close'].values, forecast_SARIMAX["SARIMA Forecast"]))
print("RMSE: ",sarimax_rmse)
