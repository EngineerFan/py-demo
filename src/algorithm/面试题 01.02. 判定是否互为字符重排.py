# -*- coding: utf-8 -*-
# @Author      : Ryan
# @Time        : 2020/11/30 22:28
# @Software    : PyCharm
# @Description : 面试题 01.02. 判定是否互为字符重排


class Solution:
    def CheckPermutation(self, s1: str, s2: str) -> bool:
        if s1 == s2 == '':
            return True
        elif s1 != s2 and len(s1) == len(s2):
            s1Set = set(list(s1))
            s2Set = set(list(s2))
            if ''.join(s1Set) == ''.join(s2Set):
                return True
            else:
                return False
        elif len(s1) != len(s2):
            return False
        else:
            return True


if __name__ == '__main__':
    so = Solution()
    s1 = 'abc'
    s2 = 'bca'
    print(so.CheckPermutation(s1, s2))
