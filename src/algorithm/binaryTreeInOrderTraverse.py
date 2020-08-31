# author  : Ryan
# datetime: 2020/8/31 14:15
# software: PyCharm

"""
description: 94. 二叉树的中序遍历

给定一个二叉树，返回它的中序 遍历。

示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,3,2]

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from typing import List


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        if root is None:
            return result

        def dfs(node: TreeNode, nodeList: List[int]):
            if node.left:
                dfs(node.left, nodeList)
            nodeList.append(node.val)
            if node.right:
                dfs(node.right, nodeList)

        dfs(root, result)
        return result
