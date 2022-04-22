# -*- coding: utf-8 -*-
# @Author      : Ryan
# @Time        : 2021/3/11 22:11
# @Software    : PyCharm
# @Description : 拉格朗日/牛顿 插值法
import pandas as pd
from scipy.interpolate import lagrange

input_file = '../../data/sale/catering_sale.xls'
output_file = '../../data/tmp/o.xls'

data = pd.read_excel(input_file)
data[u'销量'][(data[u'销量'] < 400) | (data[u'销量'] > 5000)] = None
print(data)

def polyinterp_column(s, n, k=5):
    y = s[list(range(n - k, n)) + list(range(n + 1, n + 1 + k))]
    y = y[y.notnull()]
    return lagrange(y.index, list(y))(n)


for i in data.columns:
    for j in range(len(data)):
        if (data[i].isnull())[j]:
            data[i][j] = polyinterp_column(data[i], j)
data.to_excel(output_file)
