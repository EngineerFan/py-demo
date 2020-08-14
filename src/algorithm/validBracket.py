# author  : Ryan
# datetime: 2020/8/14 13:00
# software: PyCharm

"""
description:  20. 有效的括号

给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:

输入: "()"
输出: true
示例 2:

输入: "()[]{}"
输出: true
示例 3:

输入: "(]"
输出: false
示例 4:

输入: "([)]"
输出: false
示例 5:

输入: "{[]}"
输出: true


"""


class Solution:
    def isValid(self, s: str) -> bool:
        sLength = len(s)
        if sLength == 0:
            return True
        l = ['()', '[]', '{}']
        lr = [')', ']', '}']
        dic1 = {'(': ')', '[': ']', '{': '}'}
        i = 0

        def deep_traverse(s: str, m: int) -> bool:
            k = 0
            while m >= 0 and s[m] not in lr:
                targetIndex = m + 2 * k + 1
                if targetIndex >= sLength:
                    return False
                if s[m] + s[targetIndex] in l:
                    m = m - 1
                    k = k + 1
                else:
                    print(m, targetIndex)
                    print(s[m] + s[targetIndex])
                    return False
            return True

        while i < sLength:
            j = i + 1
            if j < sLength and s[j] == dic1.get(s[i]):
                if not deep_traverse(s, i):
                    return False
                i = j + i + 1
                if i >= sLength:
                    return True
            else:
                i = i + 1
        return False


if __name__ == '__main__':
    so = Solution()
    s = "(([]){})"
    print(so.isValid(s))
