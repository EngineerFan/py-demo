# author  : Ryan
# datetime: 2020/9/3 20:50
# software: PyCharm

"""
description:704. 二分查找

给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。


示例 1:

输入: nums = [-1,0,3,5,9,12], target = 9
输出: 4
解释: 9 出现在 nums 中并且下标为 4
示例 2:

输入: nums = [-1,0,3,5,9,12], target = 2
输出: -1
解释: 2 不存在 nums 中因此返回 -1

"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = int((high - low) / 2) + low
            if nums[mid] < target:
                low = low + 1
            elif nums[mid] > target:
                high = mid - 1
                print(high)
            else:
                return mid
        return -1


if __name__ == '__main__':
    so = Solution()
    print(so.search([-1, 0, 3, 5, 9, 12], 2))
