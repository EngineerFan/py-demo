# -*- coding: utf-8 -*-
# @Author      : Ryan
# @Time        : 2020/8/6 22:57
# @Software    : PyCharm
# @Description : 5. 最长回文子串

'''

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"

'''


class Solution:
    def longestPalindrome(self, s: str) -> str:
        stringList = list(str(s))
        maxLength = 0
        max_list = []
        length = len(stringList)
        if length == 1:
            return s
        for i in range(length):
            for j in range(i + 1, length):
                if (j - i == 1 or j - i == 2) and stringList[j] == stringList[i]:
                    if j - i > maxLength:
                        maxLength = j - i
                        max_list = stringList[i:(j + 1)]
                elif j - i == 1 and stringList[j] != stringList[i]:
                    continue
                elif j - i > 2 and stringList[j] == stringList[i]:
                    maxLength = j - i
                    max_list = stringList[i:(j + 1)]
                else:
                    break

        if maxLength != 0:
            return ''.join(max_list)
        return s[0:1]


if __name__ == '__main__':
    so = Solution()
    string = ""
    print(so.longestPalindrome(string))
