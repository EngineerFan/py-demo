# author  : Ryan
# datetime: 2020/9/29 18:55
# software: PyCharm

"""
description: 485. 最大连续1的个数

给定一个二进制数组， 计算其中最大连续1的个数。

示例 1:

输入: [1,1,0,1,1,1]
输出: 3
解释: 开头的两位和最后的三位都是连续1，所以最大连续1的个数是 3.
注意：

输入的数组只包含 0 和1。
输入数组的长度是正整数，且不超过 10,000。

"""
from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        length = len(nums)
        start, stop, maxNums = -1, -1, 0
        for i in range(length):
            if start == -1 and nums[i] == 1:
                start = i
                if start == length - 1:
                    maxNums = max(maxNums, 1)

            elif start != -1 and nums[i] != 1:
                stop = i
                if stop - start >= length / 2:
                    return stop - start
                else:
                    maxNums = max(maxNums, stop - start)
                    start, stop = -1, -1
            elif start == 0 and nums[i] != 1 and i != length - 1:
                maxNums, stop = max(maxNums, i - start), -1
            elif start != -1 and i == length - 1 and nums[i] == 1:
                maxNums, stop = max(maxNums, i - start + 1), -1
            else:
                continue
        return maxNums


if __name__ == '__main__':
    so = Solution()
    nums = [1, 1, 0, 1]
    print(so.findMaxConsecutiveOnes(nums))
