# author  : Ryan
# datetime: 2021/2/18 14:50
# software: PyCharm

"""
description: conv2d demo

"""
# from __future__ import print_function

import torch as t

from IPython import display
from matplotlib import pyplot as plt
import numpy as np
from torch.autograd import Variable as V

# a = t.arange(0, 16).view(4, 4)


# print(a)
# index = t.LongTensor([[0, 1, 2, 3]])
# print(a.gather(0, index))
# a = t.tensor([[1, 2, 3], [4, 5, 6]])
# index_1 = t.LongTensor([[0, 1], [2, 0]])
# out = a.gather(1, index_1)
# print(out)
# out = t.Tensor()
# out.scatter_(1, index_1)
# print(a)
# index = t.LongTensor([[0, 1, 2, 3], [3, 2, 1, 0]]).t()
# print(index)
# b = a.gather(1, index)
# print(b)
# c = t.zeros(4, 4, dtype=torch.long)
# print(c.scatter_(1, index, b))

# t.set_default_tensor_type('torch.IntTensor')
# a = t.Tensor(2, 3)
# print(a.new_empty(2, 3))
# a = t.arange(0., 6.).view(2, 3)
# print(a)
# print(t.clamp(a, min=3))
# print(t.pow(a, 2))
# print(t.fmod(a, 3))
# print(t.cos(a))

# b = t.ones(2, 3)
# print(b)
# print('--' * 20)
# print(b.sum(dim=0, keepdim=False))
# print(b.sum(dim=1))

# a = t.arange(0, 6).view(2, 3)
# print(a)
# print(a.cumsum(dim=1))

# a = t.linspace(0, 15, 6).view(6, 1)
# b = t.linspace(15, 0, 6).view(2, 3)
# print(a)
# print('-' * 50)
# print(b)
# print('-' * 50)
# print(t.max(a, b))
#
# print(a[a > b])

# print(a)
# print(t.trace(a))


# a = t.arange(0, 6)
# b = a.view(2, 3)
# print(a.storage())
# print(b.storage())
# print(id(a.storage()) == id(b.storage()))
# c = a[:2]
# print(c.storage())

# print(np.linalg.inv(np.array([[1, 2, 1, 0], [-1, -3, 0, 1]])))


def get_fake_data(batch_size=8):
    x = t.rand(batch_size, 1) * 20
    y = x * 2 + (1 + t.rand(batch_size, 1)) * 3
    return x, y


w = t.rand(1, 1)
b = t.zeros(1, 1)
lr = 0.001

for ii in range(20000):
    x, y = get_fake_data()
    # 定义预判方程
    y_pred = x.mm(w) + b.expand_as(y)

    y_pred.backward()

    # 定义误差
    loss = 0.5 * (y_pred - y) ** 2
    loss = loss.sum()

    # 定义误差求偏导
    d_loss = 1
    d_y_pred = d_loss * (y_pred - y)
    d_w = x.t().mm(d_y_pred)
    d_b = d_y_pred.sum()

    w = t.sub(w, d_w * lr)
    b = t.sub(b, d_b * lr)

    if ii % 1000 == 0:
        display.clear_output(wait=True)
        x = t.arange(0, 20).view(-1, 1)
        y = x.float().mm(w) + b.float().expand_as(x)
        plt.plot(x.numpy(), y.numpy())

        x2, y2 = get_fake_data(batch_size=20)
        plt.scatter(x2.numpy(), y2.numpy())

        plt.xlim(0, 20)
        plt.ylim(0, 41)
        plt.show()
        plt.pause(0.5)

print(w.squeeze().item(), b.squeeze().item())
