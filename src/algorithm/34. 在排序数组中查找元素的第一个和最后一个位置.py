# author  : Ryan
# datetime: 2020/12/1 14:41
# software: PyCharm

"""
description: 34. 在排序数组中查找元素的第一个和最后一个位置

给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

如果数组中不存在目标值 target，返回 [-1, -1]。

进阶：

你可以设计并实现时间复杂度为 O(log n) 的算法解决此问题吗？

"""

from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        if len(nums) == 1:
            if target == nums[0]:
                return [0, 0]
            return [-1, -1]
        low, high = 0, len(nums) - 1
        while True:
            mid = (low + high) // 2
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] == target:
                break
            else:
                high = mid - 1
            if low > high:
                low, high = -1, -1
                break
        if low == -1 and high == -1:
            return [low, high]
        result = []
        for i in range(low, high + 1):
            if target == nums[i]:
                if len(result) == 0:
                    result.append(i)
                if i + 1 > len(nums) - 1:
                    result.append(i)
                    break
                if nums[i + 1] != target:
                    result.append(i)
        return result


if __name__ == '__main__':
    so = Solution()
    nums = [1,4]
    target = 4
    print(so.searchRange(nums, target))
