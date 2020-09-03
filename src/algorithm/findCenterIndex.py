# author  : Ryan
# datetime: 2020/9/3 20:17
# software: PyCharm

"""
description: 724. 寻找数组的中心索引

给定一个整数类型的数组 nums，请编写一个能够返回数组 “中心索引” 的方法。

我们是这样定义数组 中心索引 的：数组中心索引的左侧所有元素相加的和等于右侧所有元素相加的和。

如果数组不存在中心索引，那么我们应该返回 -1。如果数组有多个中心索引，那么我们应该返回最靠近左边的那一个。

 

示例 1：

输入：
nums = [1, 7, 3, 6, 5, 6]
输出：3
解释：
索引 3 (nums[3] = 6) 的左侧数之和 (1 + 7 + 3 = 11)，与右侧数之和 (5 + 6 = 11) 相等。
同时, 3 也是第一个符合要求的中心索引。
示例 2：

输入：
nums = [1, 2, 3]
输出：-1
解释：
数组中不存在满足此条件的中心索引。

"""
from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        length = len(nums)
        for i in range(length):
            print(nums[:i], ' 求和结果： ', sum(nums[:i]))
            print(nums[i + 1:], ' 求和结果： ', sum(nums[i + 1:]))
            print('-' * 100)
            if sum(nums[:i]) == sum(nums[i + 1:]):
                return i
        return -1


if __name__ == '__main__':
    so = Solution()
    nums = [1, 7, 3, 6, 5, 6]
    print(so.pivotIndex(nums))
