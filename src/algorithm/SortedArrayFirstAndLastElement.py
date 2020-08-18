# author  : Ryan
# datetime: 2020/8/18 10:25
# software: PyCharm

"""
description: 34. 在排序数组中查找元素的第一个和最后一个位置


给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

你的算法时间复杂度必须是 O(log n) 级别。

如果数组中不存在目标值，返回 [-1, -1]。

示例 1:

输入: nums = [5,7,7,8,8,10], target = 8
输出: [3,4]
示例 2:

输入: nums = [5,7,7,8,8,10], target = 6
输出: [-1,-1]

"""
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        if length == 0:
            return [-1, -1]
        result = []

        def binarySearch(index: int, target: int, indexList: List) -> List:
            if target < nums[index] and index > 0:
                return binarySearch(int(index / 2), target, indexList)
            if target != nums[index] and index == 0:
                indexList = [-1, -1]
                return indexList
            elif target > nums[index] and index < length - 1:
                return binarySearch(index + int((length - index) / 2) - 1, target, indexList)
            elif target > nums[index] and index == length - 1:
                indexList = [-1, -1]
                return indexList
            elif target == nums[index]:
                indexList.append(index)
                if index + 1 > length - 1:
                    indexList.append(index)
                elif nums[index + 1] == target:
                    indexList.append(index + 1)
                else:
                    indexList.append(index)
                return indexList

        if length >= 2:
            result = binarySearch(int(length / 2) - 1, target, result)
        else:
            result = binarySearch(int(length / 2), target, result)
        return result


if __name__ == '__main__':
    s = Solution()
    nums = [1, 4]
    target = 4
    print(s.searchRange(nums, target))
