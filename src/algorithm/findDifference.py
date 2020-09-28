# author  : Ryan
# datetime: 2020/9/27 19:18
# software: PyCharm

"""
description:  389. 找不同

给定两个字符串 s 和 t，它们只包含小写字母。

字符串 t 由字符串 s 随机重排，然后在随机位置添加一个字母。

请找出在 t 中被添加的字母。

 

示例:

输入：
s = "abcd"
t = "abcde"

输出：
e

解释：
'e' 是那个被添加的字母。

"""


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sList = list(s)
        sList.sort()
        tList = list(t)
        tList.sort()
        sLength = len(sList)
        for i in range(sLength):
            if sList[i] != tList[i]:
                return tList[i]
        return tList[sLength]
