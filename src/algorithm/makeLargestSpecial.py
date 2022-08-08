# -*- coding: utf-8 -*-
# @Author      : Ryan
# @Time        : 2022/8/8 22:49
# @Software    : PyCharm
# @Description :761. 特殊的二进制序列


class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        if len(s) <= 2:
            return s
        result = left = 0
        subList = list()
        for i, ch in enumerate(s):
            if ch == '1':
                result += 1
            else:
                result -= 1
                if result == 0:
                    subList.append('1' + self.makeLargestSpecial(s[left + 1:i]) + '0')
                    left = i + 1
        subList.sort(reverse=True)
        return ''.join(subList)


if __name__ == '__main__':
    so = Solution()
    print(so.makeLargestSpecial("11011000"))
