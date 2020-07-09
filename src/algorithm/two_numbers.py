# -*- coding: utf-8 -*-
# @Author      : Ryan
# @Time        : 2020/7/9 19:10
# @Software    : PyCharm
# @Description :

initial_array = [5, 6, 1, 3, 4, 7, 8]
target = 7

for i in range(len(initial_array)):
    tmp = target - initial_array[i]
    for j in range(i + 1, len(initial_array)):
        if tmp == initial_array[j]:
            print(initial_array[i], initial_array[j])
