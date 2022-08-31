from typing import *


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        index = 0
        for p in popped:
            if stack and p == stack[-1]:
                stack.pop()
            else:
                while index < len(popped):
                    if pushed[index] == p:
                        index += 1
                        break
                    else:
                        stack.append(pushed[index])
                        index += 1
        print(stack)
        print(index)


if __name__ == '__main__':
    so = Solution()
    print(so.validateStackSequences([1, 2, 3, 4, 5], [4, 5, 3, 2, 1]))
