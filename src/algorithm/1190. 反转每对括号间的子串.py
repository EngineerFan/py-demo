# -*- coding: utf-8 -*-
# @Author      : Ryan
# @Time        : 2021/5/26 19:37
# @Software    : PyCharm
# @Description : 1190. 反转每对括号间的子串


class Solution:
    def reverseParentheses(self, s: str) -> str:
        i =  0
        stack = []
        while i < len(s):
            if s[i] == ')':
                tmp = []
                while stack[-1] != '(':
                    tmp.append(stack.pop())
                stack.pop()
                for t in tmp:
                    stack.append(t)
            else:
                stack.append(s[i])
            i += 1
        return ''.join(stack)

so = Solution()
s = "(ed(et(oc))el)"
print(so.reverseParentheses(s))
