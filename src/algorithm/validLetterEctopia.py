# author  : Ryan
# datetime: 2020/8/20 13:04
# software: PyCharm

"""
description: 242. 有效的字母异位词

给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

示例 1:

输入: s = "anagram", t = "nagaram"
输出: true
示例 2:

输入: s = "rat", t = "car"
输出: false
说明:
你可以假设字符串只包含小写字母。

"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sLength = len(s)
        tLength = len(t)
        if sLength != tLength:
            return False
        tList = list(t)
        result = True
        resultList = [False for n in range(sLength)]
        for i in range(tLength):
            if t[i] == s[i]:
                resultList[i] = True
                continue
            tLetterNums = tList.count(t[i])


if __name__ == '__main__':
    so = Solution()
    s = 'anagram'
    t = 'nagaram'
    print(so.isAnagram(s, t))
