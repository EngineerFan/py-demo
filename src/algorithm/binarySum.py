# author  : Ryan
# datetime: 2020/8/18 16:31
# software: PyCharm

"""
description: 67. 二进制求和

给你两个二进制字符串，返回它们的和（用二进制表示）。

输入为 非空 字符串且只包含数字 1 和 0。

 

示例 1:

输入: a = "11", b = "1"
输出: "100"
示例 2:

输入: a = "1010", b = "1011"
输出: "10101"
 

提示：

每个字符串仅由字符 '0' 或 '1' 组成。
1 <= a.length, b.length <= 10^4
字符串如果不是 "0" ，就都不含前导零。


"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        prefix = '0b'
        a = prefix + a
        b = prefix + b
        r = str(bin(int(a, 2) + int(b, 2))).replace('0b', '')
        return r


if __name__ == '__main__':
    s = Solution()
    a = '11'
    b = '1'
    print(s.addBinary(a, b))
