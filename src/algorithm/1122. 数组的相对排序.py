# -*- coding: utf-8 -*-
# @Author      : Ryan
# @Time        : 2020/11/14 13:50
# @Software    : PyCharm
# @Description : 1122. 数组的相对排序

"""
给你两个数组，arr1 和 arr2，

arr2 中的元素各不相同
arr2 中的每个元素都出现在 arr1 中
对 arr1 中的元素进行排序，使 arr1 中项的相对顺序和 arr2 中的相对顺序相同。未在 arr2 中出现过的元素需要按照升序放在 arr1 的末尾。

 

示例：

输入：arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
输出：[2,2,2,1,4,3,3,9,6,7,19]
 

提示：

arr1.length, arr2.length <= 1000
0 <= arr1[i], arr2[i] <= 1000
arr2 中的元素 arr2[i] 各不相同
arr2 中的每个元素 arr2[i] 都出现在 arr1 中

"""
from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr2Length = len(arr2)
        arr1Length = len(arr1)
        result = []
        needRemoveIndexList = []
        for i in range(arr2Length):
            for j in range(arr1Length):
                if arr1[j] == arr2[i]:
                    result.append(arr1[j])
                    needRemoveIndexList.append(j)

        needRemoveIndexList.sort()
        noneList = []
        for k in range(arr1Length):
            try:
                needRemoveIndexList.index(k)
            except ValueError:
                noneList.append(arr1[k])
        noneList.sort()
        for n in noneList:
            result.append(n)
        return result


if __name__ == '__main__':
    so = Solution()
    arr1 = [28, 6, 22, 8, 44, 17]
    arr2 = [22, 28, 8, 6]
    print(so.relativeSortArray(arr1, arr2))
