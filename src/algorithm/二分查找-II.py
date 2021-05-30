# -*- coding: utf-8 -*-
# @Author      : Ryan
# @Time        : 2021/5/30 15:04
# @Software    : PyCharm
# @Description : 二分查找-II

#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 如果目标值存在返回下标，否则返回 -1
# @param nums int整型一维数组
# @param target int整型
# @return int整型
#
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums)
        if end == 0:
            return -1
        result = -1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                result = mid
                end = mid - 1
        return result


so = Solution()
nums = [1, 1, 1, 1, 1]
target = 1
print(so.search(nums=nums, target=target))
