# author  : Ryan
# datetime: 2022/3/23 19:38
# software: PyCharm

"""
description: 105. 从前序与中序遍历序列构造二叉树

"""
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        pass
