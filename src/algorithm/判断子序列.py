# -*- coding: utf-8 -*-
# @Author      : Ryan
# @Time        : 2021/7/15 20:41
# @Software    : PyCharm
# @Description : 判断子序列

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sList = list(s)
        tList = list(t)
        sLength = len(sList)
        tLength = len(tList)
        if sLength == 0 or tLength == 0:
            return False
        result = False
        j = 0
        for i in range(len(tList)):
            if j < sLength and tList[i] == sList[j]:
                j += 1
        if j == sLength:
            return True
        return False


so = Solution()
s = "abc"
t = "ahbgdc"
print(so.isSubsequence(s, t))
