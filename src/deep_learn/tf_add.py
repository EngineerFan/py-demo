# author  : Ryan
# datetime: 2020/7/29 11:07
# software: PyCharm

"""
description: tf add

"""
import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

a = tf.constant([1., 2.], name='a')
b = tf.constant([2., 3.], name='b')
result = a + b
print(result)
