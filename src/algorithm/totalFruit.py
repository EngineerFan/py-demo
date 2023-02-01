'''
你正在探访一家农场，农场从左到右种植了一排果树。这些树用一个整数数组 fruits 表示，其中 fruits[i] 是第 i 棵树上的水果 种类 。

你想要尽可能多地收集水果。然而，农场的主人设定了一些严格的规矩，你必须按照要求采摘水果：

你只有 两个 篮子，并且每个篮子只能装 单一类型 的水果。每个篮子能够装的水果总量没有限制。
你可以选择任意一棵树开始采摘，你必须从 每棵 树（包括开始采摘的树）上 恰好摘一个水果 。采摘的水果应当符合篮子中的水果类型。每采摘一次，你将会向右移动到下一棵树，并继续采摘。
一旦你走到某棵树前，但水果不符合篮子的水果类型，那么就必须停止采摘。
给你一个整数数组 fruits ，返回你可以收集的水果的 最大 数目。

输入：fruits = [1,2,1]
输出：3
解释：可以采摘全部 3 棵树。

输入：fruits = [0,1,2,2]
输出：3
解释：可以采摘 [1,2,2] 这三棵树。
如果从第一棵树开始采摘，则只能采摘 [0,1] 这两棵树。

输入：fruits = [1,2,3,2,2]
输出：4
解释：可以采摘 [2,3,2,2] 这四棵树。
如果从第一棵树开始采摘，则只能采摘 [1,2] 这两棵树


输入：fruits = [3,3,3,1,2,1,1,2,3,3,4]
输出：5
解释：可以采摘 [1,2,1,1,2] 这五棵树。

1 <= fruits.length <= 105
0 <= fruits[i] < fruits.length

'''

from typing import *
from collections import *


class Solution:

    def totalFruit(self, fruits: List[int]) -> int:
        maxResult = -1
        length = len(fruits)
        i = 0
        while i < length:
            one = two = fruits[i]
            count = 1
            flag = False
            twoJ = -1
            for j in range(i, length):
                if fruits[j] == one or fruits[j] == two:
                    if j == length - 1:
                        flag = True
                    continue
                else:
                    if count < 2:
                        count += 1
                        two, twoJ = fruits[j], j
                        if j == length - 1:
                            flag = True
                    else:
                        print(fruits[i:j])
                        maxResult = max(len(fruits[i:j]), maxResult)
                        tmp = fruits[j - 1]
                        tmpFlag = None
                        if tmp == fruits[i]:
                            tmpFlag = fruits[i]
                        else:
                            tmpFlag = tmp
                        for k in range(j - 1, 0, -1):
                            if fruits[k] != tmpFlag:
                                i = k
                                break
                        break
            if flag:
                maxResult = max(len(fruits[i:]), maxResult)
                break
            i += 1
        if maxResult == -1:
            maxResult = len(fruits)
        return maxResult


if __name__ == '__main__':
    so = Solution()
    print(so.totalFruit(fruits=[0, 1, 6, 6, 4, 4, 6]))
