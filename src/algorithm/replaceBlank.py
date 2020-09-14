# -*- coding: utf-8 -*-
# @Author      : Ryan
# @Time        : 2020/9/13 18:38
# @Software    : PyCharm
# @Description : 剑指 Offer 05. 替换空格
'''
请实现一个函数，把字符串 s 中的每个空格替换成"%20"。

 

示例 1：

输入：s = "We are happy."
输出："We%20are%20happy."
 

限制：

0 <= s 的长度 <= 10000

'''


class Solution:
    def replaceSpace(self, s: str) -> str:
        sList = list(s)
        for i in range(len(sList)):
            if sList[i] == ' ':
                sList[i] = sList[i].replace(' ', '%20')
        return ''.join(sList)


if __name__ == '__main__':
    so = Solution()
    s = "We are happy."
    print(so.replaceSpace(s))
