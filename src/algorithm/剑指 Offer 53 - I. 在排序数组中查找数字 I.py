# -*- coding: utf-8 -*-
# @Author      : Ryan
# @Time        : 2021/7/16 13:20
# @Software    : PyCharm
# @Description : 剑指 Offer 53 - I. 在排序数组中查找数字 I

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end, count = 0, len(nums) - 1, 0
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                count += 1
                for i in range(mid - 1, start - 1, -1):
                    if nums[i] != target:
                        break
                    count += 1
                for j in range(mid + 1, end + 1):
                    if nums[j] != target:
                        break
                    count += 1
                break
        return count


so = Solution()
nums = [5, 7, 7, 8, 8, 10]
target = 8
print(so.search(nums, target))
