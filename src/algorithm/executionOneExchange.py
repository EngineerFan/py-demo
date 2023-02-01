'''
输入：s1 = "bank", s2 = "kanb"
输出：true
解释：例如，交换 s2 中的第一个和最后一个字符可以得到 "bank"


输入：s1 = "attack", s2 = "defend"
输出：false
解释：一次字符串交换无法使两个字符串相等


输入：s1 = "kelb", s2 = "kelb"
输出：true
解释：两个字符串已经相等，所以不需要进行字符串交换

输入：s1 = "abcd", s2 = "dcba"
输出：false

1 <= s1.length, s2.length <= 100
s1.length == s2.length
s1 和 s2 仅由小写英文字母组成

'''

from typing import *


class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        s1Counter = Counter(list(s1))
        s2Counter = Counter(list(s2))
        print('s1C: ', s1Counter)
        print('s2C: ', s2Counter)
        for k, v in enumerate(s1):
            for jk, jv in enumerate(s2):
                if v == jv:
                    pass


if __name__ == '__main__':
    so = Solution()
    print(so.areAlmostEqual(s1='attack', s2='defend'))
