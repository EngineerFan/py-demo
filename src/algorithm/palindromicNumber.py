# -*- coding: utf-8 -*-
# @Author      : Ryan
# @Time        : 2020/8/12 22:49
# @Software    : PyCharm
# @Description : 回文数


'''
9. 回文数

判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

示例 1:

输入: 121
输出: true
示例 2:

输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
示例 3:

输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数

'''


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x == 0:
            return True
        if str(x) == str(x)[::-1]:
            return True
        return False


if __name__ == '__main__':
    so = Solution()
    number = 123
    print(so.isPalindrome(number))
