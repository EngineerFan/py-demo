# author  : Ryan
# datetime: 2020/8/11 13:21
# software: PyCharm

"""
description: 整数反转

给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:

输入: 123
输出: 321
 示例 2:

输入: -123
输出: -321
示例 3:

输入: 120
输出: 21
注意:

假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。

"""


class Solution:
    def reverse(self, x: int) -> int:
        x = int(str(x)[::-1] if x >= 0 else -int(str(-x)[::-1]))
        return x if 2147483648 > x >= -2147483648 else 0


if __name__ == '__main__':
    so = Solution()
    x = 100
    print(so.reverse(x))
