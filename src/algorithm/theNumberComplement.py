# author  : Ryan
# datetime: 2020/10/9 13:05
# software: PyCharm

"""
description: 476. 数字的补数

给定一个正整数，输出它的补数。补数是对该数的二进制表示取反。

 

示例 1:

输入: 5
输出: 2
解释: 5 的二进制表示为 101（没有前导零位），其补数为 010。所以你需要输出 2 。
示例 2:

输入: 1
输出: 0
解释: 1 的二进制表示为 1（没有前导零位），其补数为 0。所以你需要输出 0 。

"""


class Solution:
    def findComplement(self, num: int) -> int:
        numString = list(bin(num)[2:])
        for i in range(len(numString)):
            if numString[i] == '1':
                numString[i] = '0'
            else:
                numString[i] = '1'
        return int(''.join(numString), 2)
