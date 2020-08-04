# -*- coding: utf-8 -*-
# @Author      : Ryan
# @Time        : 2020/7/9 19:10
# @Software    : PyCharm
# @Description :
'''

给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。


示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

'''
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_length = len(nums)
        result = list()
        for i in range(nums_length - 1):
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            a = i
            real_find = target - nums[a]
            try:
                b = nums.index(real_find, i + 1, nums_length)
                return [a, b]
            except ValueError:
                continue

        return result


if __name__ == '__main__':
    so = Solution()
    array = [3, 3]
    target = 6
    print(so.twoSum(array, target=target))
