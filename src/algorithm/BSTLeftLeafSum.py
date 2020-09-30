# author  : Ryan
# datetime: 2020/9/30 8:44
# software: PyCharm

"""
description: 404. 左叶子之和

计算给定二叉树的所有左叶子之和。

示例：

    3
   / \
  9  20
    /  \
   15   7

在这个二叉树中，有两个左叶子，分别是 9 和 15，所以返回 24

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from typing import List


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:

        resultList = [0]
        if not root or (not root.left and not root.right):
            return resultList[0]

        def dfs(root: TreeNode, resultList: List[int]) -> None:
            if not root:
                return
            if root.left:
                if not root.left.left and not root.left.right:
                    resultList[0] = resultList[0] + root.left.val
                else:
                    dfs(root.left, resultList)
            if root.right:
                dfs(root.right, resultList)

        dfs(root, resultList)
        return resultList[0]
