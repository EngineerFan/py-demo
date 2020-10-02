# author  : Ryan
# datetime: 2020/10/1 9:16
# software: PyCharm

"""
description: 414. 第三大的数

给定一个非空数组，返回此数组中第三大的数。如果不存在，则返回数组中最大的数。要求算法时间复杂度必须是O(n)。

示例 1:

输入: [3, 2, 1]

输出: 1

解释: 第三大的数是 1.
示例 2:

输入: [1, 2]

输出: 2

解释: 第三大的数不存在, 所以返回最大的数 2 .
示例 3:

输入: [2, 2, 3, 1]

输出: 1

解释: 注意，要求返回第三大的数，是指第三大且唯一出现的数。
存在两个值为2的数，它们都排第二。

"""
from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        length = len(nums)
        if length < 3:
            return max(nums)
        nums.sort()
        maxVal, threshold, count = 0, -1, 0
        for i in range(length - 1, -1, -1):
            if i == length - 1:
                maxVal = nums[i]
                count = 1
            else:
                if nums[i] < nums[i + 1]:
                    count += 1
                    if count == 3:
                        return nums[i]
        return maxVal


if __name__ == '__main__':
    so = Solution()
    nums = [2, 2, 3, 1]
    print(so.thirdMax(nums))
