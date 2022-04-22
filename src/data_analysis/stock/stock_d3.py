# -*- coding: utf-8 -*-
# @Author      : Ryan
# @Time        : 2021/9/30 22:09
# @Software    : PyCharm
# @Description :

from stocker import Stocker
import matplotlib.pyplot as plt

amazon = Stocker(ticker='AMZN')
model, model_data = amazon.create_prophet_model(days=90)
amazon.evaluate_prediction()
amazon.changepoint_prior_analysis(changepoint_priors=[0.001, 0.05, 0.1, 0.2])
amazon.changepoint_prior_validation(start_date='2016-01-04', end_date='2017-01-03',
                                    changepoint_priors=[0.001, 0.05, 0.1, 0.2])
