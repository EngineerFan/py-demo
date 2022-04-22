# -*- coding: utf-8 -*-
# @Author      : Ryan
# @Time        : 2021/6/8 09:20
# @Software    : PyCharm
# @Description :


class Solution:
    def replaceSpace(self, s: str) -> str:
        print(len(s))
        result = ''
        for i in range(len(s)):
            if s[i] == ' ':
                # print('come here ???')
                result = s.replace(' ', '%20', 1)
        return result


so = Solution()
s = "     "
print(so.replaceSpace(s))
