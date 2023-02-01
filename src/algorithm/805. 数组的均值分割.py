"""
给定你一个整数数组 nums

我们要将 nums 数组中的每个元素移动到 A 数组 或者 B 数组中，使得 A 数组和 B 数组不为空，并且 average(A) == average(B) 。

如果可以完成则返回true ， 否则返回 false  。

注意：对于数组 arr ,  average(arr) 是 arr 的所有元素除以 arr 长度的和。

"""

"""
 a = [1,4,5,8]
 b = [2,3,6,7]
 
 
 从集合中任意选出一批数字，与剩余数据均值相等，则满足要求
 

"""


from typing import *


class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        pass


if __name__ == '__main__':
    so = Solution()
    print(so.splitArraySameAverage(nums=[1, 2, 3, 4, 5, 6, 7, 8]))
