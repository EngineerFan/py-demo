# author  : Ryan
# datetime: 2020/10/9 8:45
# software: PyCharm

"""
description: 461. 汉明距离

两个整数之间的汉明距离指的是这两个数字对应二进制位不同的位置的数目。

给出两个整数 x 和 y，计算它们之间的汉明距离。

注意：
0 ≤ x, y < 231.

示例:

输入: x = 1, y = 4

输出: 2

解释:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

上面的箭头指出了对应二进制位不同的位置。

"""


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xString, yString = str(bin(x)[2:]), str(bin(y)[2:])
        xLength, yLength = len(xString), len(yString)

        result = 0
        if xLength < yLength:
            j = xLength - 1
            for i in range(yLength - 1, -1, -1):
                if j == -1:
                    if yString[i] == '1':
                        result += 1
                    continue
                if xString[j] != yString[i]:
                    result += 1
                j -= 1
        elif xLength > yLength:
            j = yLength - 1
            for i in range(xLength - 1, -1, -1):
                if j == -1:
                    if xString[i] == '1':
                        result += 1
                    continue
                if yString[j] != xString[i]:
                    result += 1
                j -= 1
        else:
            for i in range(xLength):
                if xString[i] != yString[i]:
                    result += 1
        return result


if __name__ == '__main__':
    so = Solution()
    print(so.hammingDistance(100, 6))
