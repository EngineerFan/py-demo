# author  : Ryan
# datetime: 2020/10/12 13:15
# software: PyCharm

"""
description: 111. 二叉树的最小深度

给定一个二叉树，找出其最小深度。

最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

说明: 叶子节点是指没有子节点的节点。

示例:

给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回它的最小深度  2.


"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        q = [root]
        minDepth, iLeft, iRight = 1, -1, -1
        midNodeList = []
        while len(q) != 0:
            node = q.pop(0)
            if node.left:
                midNodeList.append(node.left)
            if node.right:
                midNodeList.append(node.right)
            if not node.left and not node.right:
                return minDepth
            if len(q) == 0 and len(midNodeList) != 0:
                minDepth += 1
                for iNode in midNodeList:
                    q.append(iNode)
                midNodeList.clear()

        return minDepth
