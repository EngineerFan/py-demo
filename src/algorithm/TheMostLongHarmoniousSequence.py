# author  : Ryan
# datetime: 2020/9/27 8:47
# software: PyCharm

"""
description: 594. 最长和谐子序列

和谐数组是指一个数组里元素的最大值和最小值之间的差别正好是1。

现在，给定一个整数数组，你需要在所有可能的子序列中找到最长的和谐子序列的长度。

示例 1:

输入: [1,3,2,2,5,2,3,7]
输出: 5
原因: 最长的和谐数组是：[3,2,2,2,3].
说明: 输入的数组长度最大不超过20,000.


"""

from typing import List


class Solution:
    """
    <b> 暴力迭代法 </b>
    numsLength = len(nums)
    maxCount = 0
    for i in range(numsLength):
        tempAddCount, tempSubCount, tempEquCount = 0, 0, 0
        remainNums = numsLength - (i + 1)
        for j in range(i + 1, numsLength):
            if nums[i] - nums[j] == 1:
                tempSubCount += 1
            elif nums[i] - nums[j] == -1:
                tempAddCount += 1
            elif nums[i] == nums[j]:
                tempEquCount += 1
        if tempEquCount == remainNums:
            break
        if tempSubCount + tempEquCount == remainNums or tempAddCount + tempEquCount == remainNums:
            maxCount = max(remainNums + 1, maxCount)
            break
        if tempSubCount + tempEquCount < tempAddCount + tempEquCount:
            maxCount = max(tempAddCount + tempEquCount + 1, maxCount)
        elif tempSubCount + tempEquCount > tempAddCount + tempEquCount:
            maxCount = max(tempSubCount + tempEquCount + 1, maxCount)
        elif tempSubCount == tempAddCount != 0:
            maxCount = max(tempSubCount + tempEquCount + 1, maxCount)
        else:
            continue
    return maxCount
    """

    def findLHS(self, nums: List[int]) -> int:
        length = len(nums)
        nums.sort()
        print('数组： ', nums, ' 对应长度： ', length)
        start, tempCount, maxCount, threshold = -1, 1, 0, -1
        i = 0
        while i < length:
            if i == 0:
                start = i
            elif nums[i] - nums[start] > 1:
                if threshold != -1:
                    # if tempCount >= length / 2:
                    #     return tempCount
                    maxCount = max(maxCount, tempCount)
                    start, i = threshold, threshold + 1
                    threshold, tempCount = -1, 1
                    continue
                else:
                    maxCount = max(maxCount, 0)
                    start = i
                    tempCount = 1
            elif nums[i] - nums[start] <= 1:
                if threshold == -1 and nums[i] - nums[start] == 1:
                    threshold = i
                tempCount += 1
            i = i + 1
        if threshold != -1:
            maxCount = max(maxCount, tempCount)
        else:
            maxCount = max(maxCount, 0)
        return maxCount


if __name__ == '__main__':
    so = Solution()
    # nums = [1, 1, 1, 1]
    # nums = [3, 2, 2, 3, 2, 1, 3, 3, 3, -2, 0, 3, 2, 1, 0, 3, 1, 0, 1, 3, 0, 3, 3]
    # nums = [1, 0, 2, 0, 1, 2, 3, 1, 1, 1, 3, 3, 3, 1, 0, 3, 0, 3, 1, 3, -1, 2, 2, 1, 1, 3, 1]
    nums = [1, 3, 2, 2, 5, 2, 3, 7]
    # nums = [1, 2, 2, 1]
    print(so.findLHS(nums))
