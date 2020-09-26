# author  : Ryan
# datetime: 2020/9/25 13:31
# software: PyCharm

"""
description: 559. N叉树的最大深度

给定一个 N 叉树，找到其最大深度。

最大深度是指从根节点到最远叶子节点的最长路径上的节点总数。

例如，给定一个 3叉树 :

 



 

我们应返回其最大深度，3。


"""


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


from typing import List


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root is None:
            return 0
        maxDepth = [1]
        tempVal = [0]

        def NST(root: 'Node', maxDepth: List[int], tempVal: List[int]) -> None:
            tempVal[0] = tempVal[0] + 1
            if root.children is None or len(root.children) == 0:
                maxDepth[0] = max(tempVal[0], maxDepth[0])
                return
            for i in range(len(root.children)):
                NST(root.children[i], maxDepth, tempVal)
                tempVal[0] -= 1

        NST(root, maxDepth, tempVal)
        return maxDepth[0]
