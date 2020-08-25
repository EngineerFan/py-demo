# author  : Ryan
# datetime: 2020/8/25 10:11
# software: PyCharm

"""
description: 滑动窗口的最大值

给定一个数组 nums 和滑动窗口的大小 k，请找出所有滑动窗口里的最大值。

示例:

输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
输出: [3,3,5,5,6,7]
解释:

  滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
 
"""
from typing import List


class Solution:
    """  方案一 暴力循环
            # length = len(nums)
            # resultList = []
            # for i in range(length):
            #     j = i + k
            #     if j > length:
            #         break
            #     tmp = i
            #     maxVal = nums[tmp]
            #     while tmp < j:
            #         maxVal = max(maxVal, nums[tmp])
            #         tmp += 1
            #     resultList.append(maxVal)
            # return resultList
    """

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        pass


if __name__ == '__main__':
    so = Solution()
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    print(so.maxSlidingWindow(nums, k))
