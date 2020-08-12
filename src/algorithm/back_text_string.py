# author  : Ryan
# datetime: 2020/8/12 19:20
# software: PyCharm

"""
description: 5. 最长回文子串

给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"


"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        thMax = 0
        start = 0
        for i in range(n):
            if i - thMax >= 1 and s[i - thMax - 1: i + 1] == s[i - thMax - 1: i + 1][::-1]:
                start = i - thMax - 1
                thMax += 2
                continue
            if i - thMax >= 0 and s[i - thMax: i + 1] == s[i - thMax: i + 1][::-1]:
                start = i - thMax
                thMax += 1
        return s[start: start + thMax]


if __name__ == '__main__':
    so = Solution()
    stringChuan = 'babad'
    print(so.longestPalindrome(stringChuan))
