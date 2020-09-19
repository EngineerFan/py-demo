# -*- coding: utf-8 -*-
# @Author      : Ryan
# @Time        : 2020/9/19 11:23
# @Software    : PyCharm
# @Description : 剑指 Offer 11. 旋转数组的最小数字

"""
剑指 Offer 11. 旋转数组的最小数字
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。

示例 1：

输入：[3,4,5,1,2]
输出：1
示例 2：

输入：[2,2,2,0,1]
输出：0
"""
from typing import List


class Solution:
    def minArray(self, numbers: List[int]) -> int:
        length = len(numbers)
        if length == 0:
            return 0
        if length == 1:
            return numbers[0]
        resultIndex = 0
        for i in range(length):
            if i != 0 and numbers[i] >= numbers[i - 1]:
                continue
            elif numbers[i] < numbers[i - 1]:
                resultIndex = i
                return numbers[resultIndex]
        return numbers[resultIndex]


if __name__ == '__main__':
    so = Solution()
    numbers = [2, 2, 2, 0, 1]
    print(so.minArray(numbers))
