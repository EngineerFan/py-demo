# author  : Ryan
# datetime: 2020/10/28 18:20
# software: PyCharm

"""
description: 1207. 独一无二的出现次数

给你一个整数数组 arr，请你帮忙统计数组中每个数的出现次数。

如果每个数的出现次数都是独一无二的，就返回 true；否则返回 false。

 

示例 1：

输入：arr = [1,2,2,1,1,3]
输出：true
解释：在该数组中，1 出现了 3 次，2 出现了 2 次，3 只出现了 1 次。没有两个数的出现次数相同。
示例 2：

输入：arr = [1,2]
输出：false
示例 3：

输入：arr = [-3,0,1,-3,1,1,1,-3,10,0]
输出：true
 

提示：

1 <= arr.length <= 1000
-1000 <= arr[i] <= 1000

"""
from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        length = len(arr)
        dictMap = {}
        for i in range(length):
            if dictMap.get(arr[i], None) is None:
                dictMap[arr[i]] = 1
            else:
                dictMap[arr[i]] = dictMap.get(arr[i]) + 1
        l = list(dictMap.values())
        lLength = len(l)
        llMap = {}
        for j in range(lLength):
            if llMap.get(str(l[j]), -1) == -1:
                llMap[str(l[j])] = 1
            else:
                return False
        return True


if __name__ == '__main__':
    so = Solution()
    arr = [1, 2, 2, 1, 1, 3]
    print(so.uniqueOccurrences(arr))
