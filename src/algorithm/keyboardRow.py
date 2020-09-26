# author  : Ryan
# datetime: 2020/9/21 9:07
# software: PyCharm

"""
description: 500. 键盘行

示例：

给定一个单词列表，只返回可以使用在键盘同一行的字母打印出来的单词。键盘如下图所示。

输入: ["Hello", "Alaska", "Dad", "Peace"]
输出: ["Alaska", "Dad"]
 

注意：

你可以重复使用键盘上同一字符。
你可以假设输入的字符串将只包含字母。

"""
from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        letterList = [['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'], ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'],
                      ['z', 'x', 'c', 'v', 'b', 'n', 'm']]
        resultList = []
        length = len(words)
        for i in range(length):
            sList = list(words[i].lower())
            legitimateVal = None
            sSet = set(sList)
            for ll in letterList:
                if sSet.issubset(ll):
                    legitimateVal = i
                    break
            if legitimateVal is not None:
                resultList.append(words[i])
        return resultList


if __name__ == '__main__':
    so = Solution()
    words = ["adsdf", "sfd"]
    print(so.findWords(words))
