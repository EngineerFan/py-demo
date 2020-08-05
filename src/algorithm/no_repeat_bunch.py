# author  : Ryan
# datetime: 2020/8/5 10:56
# software: PyCharm

"""
description: 3. 无重复字符的最长子串


给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lMax = 0
        lTmpMax = 0
        if len(s) == 0:
            return lMax
        l = list(str(s))
        lLength = len(l)
        for i in range(lLength):
            if i + 1 < lLength and l[i] == l[i + 1]:
                lMax = max(lTmpMax, lMax)
                continue
            start = i
            end = i
            for j in range(i, lLength):
                end = j
                try:
                    l.index(l[j], start, end)
                    # 存在与过去相同字符
                    lTmpMax = end - start
                    lMax = max(lTmpMax, lMax)
                    lTmpMax = lMax
                    # print(lMax)
                    break
                except ValueError:
                    if i == 0 and j == lLength - 1:
                        lTmpMax = (end - start) + 1
                        lMax = max(lTmpMax, lMax)
                        lTmpMax = lMax
                        return lMax
                    else:
                        lTmpMax = (end - start) + 1
                        lMax = max(lTmpMax, lMax)
                        lTmpMax = lMax
        return lMax


if __name__ == '__main__':
    so = Solution()
    string = "pwwkew"
    print(so.lengthOfLongestSubstring(string))
