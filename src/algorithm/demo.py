# -*- coding: utf-8 -*-
# @Author      : Ryan
# @Time        : 2020/7/24 14:00
# @Software    : PyCharm
# @Description : demo


def fib(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)
