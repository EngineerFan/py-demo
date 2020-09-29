# author  : Ryan
# datetime: 2020/9/29 18:41
# software: PyCharm

"""
description: 226. 翻转二叉树

翻转一棵二叉树。

示例：

输入：

     4
   /   \
  2     7
 / \   / \
1   3 6   9
输出：

     4
   /   \
  7     2
 / \   / \
9   6 3   1

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        q = [root]
        newTreeRootNode = root
        while len(q) != 0:
            node = q.pop(0)
            tempL = node.left
            tempR = node.right
            node.left = tempR
            node.right = tempL
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return newTreeRootNode
