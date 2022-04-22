# -*- coding: utf-8 -*-
# @Author      : Ryan
# @Time        : 2021/9/29 12:39
# @Software    : PyCharm
# @Description :


import pandas as pd
from prophet import Prophet
from stocker import Stocker

microsoft = Stocker(ticker='MSFT')
print(microsoft)