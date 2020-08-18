# author  : Ryan
# datetime: 2020/8/17 16:46
# software: PyCharm

"""
description: 58. 最后一个单词的长度

给定一个仅包含大小写字母和空格 ' ' 的字符串 s，返回其最后一个单词的长度。如果字符串从左向右滚动显示，那么最后一个单词就是最后出现的单词。

如果不存在最后一个单词，请返回 0 。

说明：一个单词是指仅由字母组成、不包含任何空格字符的 最大子字符串。


"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        result = s.strip()
        print(result)
        if len(result) == 0:
            return 0
        result = result.split(' ')
        return len(result[-1])


if __name__ == '__main__':
    so = Solution()
    s = 'H  '
    print(so.lengthOfLastWord(s))
