# author  : Ryan
# datetime: 2020/8/18 16:07
# software: PyCharm

"""
description: 66. 加一

给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。

示例 1:

输入: [1,2,3]
输出: [1,2,4]
解释: 输入数组表示数字 123。
示例 2:

输入: [4,3,2,1]
输出: [4,3,2,2]
解释: 输入数组表示数字 4321。


"""
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        new_digits = [str(s) for s in digits]
        number = int(''.join(new_digits))
        number = number + 1
        strNumber = str(number)
        resultStringList = list(strNumber)
        return [int(rs) for rs in resultStringList]


if __name__ == '__main__':
    s = Solution()
    digits = [1, 2, 3]
    print(s.plusOne(digits))
