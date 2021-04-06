# author  : Ryan
# datetime: 2021/4/6 18:19
# software: PyCharm

"""
description: 80. 删除有序数组中的重复项 II

"""

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j = 0, 0
        count = 1
        while j < len(nums):
            j += 1
            if j < len(nums) and nums[j] == nums[i]:
                count += 1
                if count >= 3:
                    nums.pop(j)
                    j -= 1
                    count -= 1
            else:
                count = 1
                i = j

        return len(nums)


so = Solution()
print(so.removeDuplicates(nums=[0, 0, 1, 1, 1, 1, 2, 3, 3]))
