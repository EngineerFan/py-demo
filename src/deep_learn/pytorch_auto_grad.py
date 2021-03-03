# author  : Ryan
# datetime: 2021/3/3 16:53
# software: PyCharm

"""
description: auto grad

"""

import torch as t
from torch.autograd import Variable as V
import numpy as np


# a = V(t.ones(3, 4), requires_grad=True)
# b = V(t.zeros(3, 4))
#
# c = t.add(a, b)
# d = c.sum()
# d.backward()


# print(a.requires_grad, b.requires_grad, c.requires_grad)
# print(a.is_leaf, b.is_leaf, c.is_leaf)

# print(d.is_leaf)


def f(x: int) -> int:
    return x ** 2 * t.exp(x)


def grad_f(x):
    return 2 * x * t.exp(x) + x ** 2 * t.exp(x)


# x = V(t.rand(3, 4), requires_grad=True)
# y = f(x)
# print(y)
#
# print(grad_f(x))


# x = V(t.rand(1), requires_grad=False)
# b = V(t.rand(1), requires_grad=True)
# w = V(t.rand(1), requires_grad=True)
#
# y = w * x
# z = y + b
#
# print(x.requires_grad, b.requires_grad, w.requires_grad)
# print(x.is_leaf, w.is_leaf, y.is_leaf, b.is_leaf, z.is_leaf)
# print(z.grad_fn)
# print('-' * 20)
# print(z.grad_fn.next_functions)
# print(z.grad_fn.next_functions[0][0] == y.grad_fn)


def abs(x):
    if x.data[0] > 0:
        return x
    else:
        return -x


# x = V(t.ones(1), requires_grad=True)
# y = abs(x)
# y.backward()
# print(x.grad)
#
# print('-' * 20)
#
# x = V(-1 * t.ones(1), requires_grad=True)
# y = abs(x)
# y.backward()
# print(x.grad)

def f(x):
    result = 1
    for ii in x:
        if ii.item() > 0:
            result = ii * result
            # print(result)
    return result


print(t.arange(-2., 4.))

x = V(t.tensor(np.arange(-2, 4)).float(), requires_grad=True)
y = f(x)

y.backward()
print(x.grad)
