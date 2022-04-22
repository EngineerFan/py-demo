# -*- coding: utf-8 -*-
# @Author      : Ryan
# @Time        : 2021/10/9 19:43
# @Software    : PyCharm
# @Description :


from pandas_datareader import naver
import pandas_datareader as pdr
import pandas as pd
import pandas_datareader.data as web
import os
df = web.DataReader('GE', 'yahoo', start='2019-09-10', end='2019-10-09')
print(df.head())
