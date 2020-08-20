# author  : Ryan
# datetime: 2020/8/20 11:30
# software: PyCharm

"""
description: 217. 存在重复元素

给定一个整数数组，判断是否存在重复元素。

如果任意一值在数组中出现至少两次，函数返回 true 。如果数组中每个元素都不相同，则返回 false 。

 

示例 1:

输入: [1,2,3,1]
输出: true
示例 2:

输入: [1,2,3,4]
输出: false
示例 3:

输入: [1,1,1,3,3,4,3,2,4,2]
输出: true

"""
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        length = len(nums)
        if length == 0:
            return False
        nums.sort()
        for i in range(length):
            if i != 0 and nums[i] == nums[i - 1]:
                return True
        return False


if __name__ == '__main__':
    so = Solution()
    nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    print(so.containsDuplicate(nums))
