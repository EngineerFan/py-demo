# author  : Ryan
# datetime: 2020/11/5 14:58
# software: PyCharm

"""
description: 127. 单词接龙

给定两个单词（beginWord 和 endWord）和一个字典，找到从 beginWord 到 endWord 的最短转换序列的长度。转换需遵循如下规则：

每次转换只能改变一个字母。
转换过程中的中间单词必须是字典中的单词。
说明:

如果不存在这样的转换序列，返回 0。
所有单词具有相同的长度。
所有单词只由小写字母组成。
字典中不存在重复的单词。
你可以假设 beginWord 和 endWord 是非空的，且二者不相同。
示例 1:

输入:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

输出: 5

解释: 一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog",
     返回它的长度 5。
示例 2:

输入:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

输出: 0

解释: endWord "cog" 不在字典中，所以无法进行转换。

"""
import string
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        res = 1
        queue = [beginWord]
        seen = set()
        next_level = set()
        wordList = set(wordList)
        length = len(beginWord)
        tag = 0
        while queue:
            num = len(queue)
            while num:
                num -= 1
                curr = queue.pop()
                curr_li = list(curr)
                for i in range(length):
                    char = curr_li[i]
                    for j in string.ascii_lowercase:
                        curr_li[i] = j
                        word = "".join(curr_li)
                        if word not in seen and word in wordList:
                            next_level.add(word)
                            if word == endWord:
                                tag = 1
                    curr_li[i] = char
            res += 1
            if tag == 1:
                break
            seen |= next_level
            queue = list(next_level)
            next_level.clear()
        return res if tag else 0


if __name__ == '__main__':
    so = Solution()
    beginWord = "hit",
    endWord = "cog",
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    print(so.ladderLength(beginWord, endWord, wordList))
