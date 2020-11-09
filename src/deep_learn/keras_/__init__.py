# -*- coding: utf-8 -*-
# @Author      : Ryan
# @Time        : 2020/10/15 21:44
# @Software    : PyCharm
# @Description : keras.Dense or layers

from keras.layers import Dense , Input


inputs = Input((8,))
layer = Dense(8)

print(layer.get_weights())


x = layer(inputs)
print(x)
print(layer.get_weights())