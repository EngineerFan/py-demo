from stocker import Stocker
import matplotlib.pyplot as plt

microsoft = Stocker(ticker='MSFT')

stock_history = microsoft.stock
# microsoft.plot_stock(start_date='2001-01-05', end_date='2002-02-05', stats=["Adj. Close"], plot_type="basic")
# microsoft.buy_and_hold(start_date='2001-01-05', end_date='2002-02-05', nshares=200)

model, model_data = microsoft.create_prophet_model()

model.plot_components(model_data)
plt.show()
print(microsoft.weekly_seasonality)
microsoft.weekly_seasonality = True
print(microsoft.weekly_seasonality)

model, model_data = microsoft.create_prophet_model(days=0)
model.plot_components(model_data)
plt.show()
microsoft.weekly_seasonality = False
microsoft.changepoint_date_analysis()
model, future = microsoft.create_prophet_model(days=180)
