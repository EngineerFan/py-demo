# author  : Ryan
# datetime: 2020/9/16 18:05
# software: PyCharm

"""
description: 796. 旋转字符串

给定两个字符串, A 和 B。

A 的旋转操作就是将 A 最左边的字符移动到最右边。 例如, 若 A = 'abcde'，在移动一次之后结果就是'bcdea' 。如果在若干次旋转操作之后，A 能变成B，那么返回True。

示例 1:
输入: A = 'abcde', B = 'cdeab'
输出: true

示例 2:
输入: A = 'abcde', B = 'abced'
输出: false
注意：

A 和 B 长度不超过 100。

"""


class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if A == '' and B == '':
            return True
        if (A == '' and B != '') or (A != '' and B == ''):
            return False
        AList = list(A)
        ALength, i = len(AList), 0
        while i < ALength:
            if ''.join(AList[i:]) + ''.join(AList[:i]) == B:
                return True
            i += 1
        return False


if __name__ == '__main__':
    so = Solution()
    A = 'abcde'
    B = 'abced'
    print(so.rotateString(A, B))
