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

#
# def abs(x):
#     if x.data[0] > 0:
#         return x
#     else:
#         return -x


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
#
# def f(x):
#     result = 1
#     for ii in x:
#         if ii.item() > 0:
#             result = ii * result
#             # print(result)
#     return result
#
#
# print(t.arange(-2., 4.))
#
# x = V(t.tensor(np.arange(-2, 4)).float(), requires_grad=True)
# y = f(x)
#
# y.backward()
# print(x.grad)

# def variable_hook(grad):
# #     print('y的梯度： \r\n', grad)
# #
# #
# # x = V(t.ones(3), requires_grad=True)
# # w = V(t.rand(3), requires_grad=True)
# #
# # y = x * w
# # hook_handle = y.register_hook(variable_hook)
# # z = y.sum()
# # z.backward()
# print(t.arange(0, 3))
# x = V(t.arange(0, 3).float(), requires_grad=True)
# y = x ** 2 + x * 2
# z = y.sum()
# z.backward()
# print(x.grad)


import base64
from Crypto.Cipher import AES

BLOCK_SIZE = 32

'''
采用AES对称加密算法
'''


def add_to_16(value):
    while len(value) % 16 != 0:
        value += '\0'
    return str.encode(value)


def encrypt_oracle():
    key = '123456'
    text = '傻鲲儿'
    aes = AES.new(add_to_16(key), AES.MODE_ECB)
    encrypt_aes = aes.encrypt(add_to_16(text), BLOCK_SIZE)
    encrypted_text = str(base64.encodebytes(encrypt_aes), encoding='utf-8')  # 执行加密并转码返回bytes
    print(encrypted_text)


# 解密方法
def decrypt_oralce():
    # 秘钥
    key = '123456'
    # 密文
    text = 'qR/TQk4INsWeXdMSbCDDdA=='
    aes = AES.new(add_to_16(key), AES.MODE_ECB)
    base64_decrypted = base64.decodebytes(text.encode(encoding='utf-8'))
    decrypted_text = str(aes.decrypt(base64_decrypted, BLOCK_SIZE), encoding='utf-8').replace('\0', '')
    print(decrypted_text)


if __name__ == '__main__':
    encrypt_oracle()
    # decrypt_oralce()
