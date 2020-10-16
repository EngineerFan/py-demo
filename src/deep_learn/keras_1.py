# author  : Ryan
# datetime: 2020/10/15 20:53
# software: PyCharm

"""
description: keras_1

"""

from tensorflow import keras
import tensorflow as tf
from tensorflow.keras import layers

model = keras.Sequential([
    #  layers.Dense(2,activation='relu',name='layer1'),
    #  layers.Dense(3,activation='relu',name='layer2'),
    #  layers.Dense(4,name='layer3')

    layers.Dense(2, name='layer1'),
    layers.Dense(3, name='layer2'),
    layers.Dense(4, name='layer3')

])
print('*' * 100)
x = tf.ones((3, 3))
y = model(x)
print(y)
