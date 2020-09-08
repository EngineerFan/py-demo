# author  : Ryan
# datetime: 2020/9/8 15:14
# software: PyCharm

"""
description: 821. 字符的最短距离

给定一个字符串 S 和一个字符 C。返回一个代表字符串 S 中每个字符到字符串 S 中的字符 C 的最短距离的数组。

示例 1:

输入: S = "loveleetcode", C = 'e'
输出: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]


"""
from typing import List


class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        resultList = []
        sList = list(S)
        length = len(sList)
        for i in range(length):
            '''
              1.向前遍历寻找最近的一个
              2.向后遍历寻找最近的一个
            '''
            if sList[i] == C:
                resultList.append(0)
                continue
            prev, after = -1, -1
            m, n = i, i
            while m < length:
                if sList[m] == C:
                    after = m
                    break
                m = m + 1
            while n >= 0:
                if sList[n] == C:
                    prev = n
                    break
                n = n - 1
            if prev != -1 and after != -1:
                if i - prev > after - i:
                    resultList.append(after - i)
                elif i - prev < after - i:
                    resultList.append(i - prev)
                else:
                    resultList.append(after - i)
            elif prev == -1 and after != -1:
                resultList.append(after - i)
            elif prev != -1 and after == - 1:
                resultList.append(i - prev)
            else:
                pass
        return resultList


if __name__ == '__main__':
    so = Solution()
    S = "baaa"
    C = 'b'
    print(so.shortestToChar(S, C))
