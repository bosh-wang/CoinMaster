# unused due to bad performance QQ

# import pandas as pd
# import yfinance as yf
# import datetime
# from datetime import date, timedelta
# today = date.today()

# d1 = today.strftime("%Y-%m-%d")
# end_date = d1
# d2 = date.today() - timedelta(days=730)
# d2 = d2.strftime("%Y-%m-%d")
# start_date = d2

# data = yf.download('BTC-USD', 
#                       start=start_date, 
#                       end=end_date, 
#                       progress=False)
# data["Date"] = data.index
# data = data[["Date", "Open", "High", "Low", "Close", "Adj Close", "Volume"]]
# data.reset_index(drop=True, inplace=True)
# print(data.head())

# from autots import AutoTS
# model = AutoTS(forecast_length=30, frequency='infer', ensemble='simple')
# model = model.fit(data, date_col='Date', value_col='Close', id_col=None)
# prediction = model.predict()
# forecast = prediction.forecast
# print(forecast)

#reference https://thecleverprogrammer.com/2021/12/27/cryptocurrency-price-prediction-with-machine-learning/