# -*- coding: utf-8 -*-
# @Author      : Ryan
# @Time        : 2020/9/6 21:23
# @Software    : PyCharm
# @Description : 859. 亲密字符串

'''
给定两个由小写字母构成的字符串 A 和 B ，只要我们可以通过交换 A 中的两个字母得到与 B 相等的结果，就返回 true ；否则返回 false 。

 

示例 1：

输入： A = "ab", B = "ba"
输出： true
示例 2：

输入： A = "ab", B = "ab"
输出： false
示例 3:

输入： A = "aa", B = "aa"
输出： true
示例 4：

输入： A = "aaaaaaabc", B = "aaaaaaacb"
输出： true
示例 5：

输入： A = "", B = "aa"
输出： false


'''


class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        pass


if __name__ == '__main__':
    so = Solution()
    A = 'ab'
    B = 'ba'
    print(so.buddyStrings(A, B))
