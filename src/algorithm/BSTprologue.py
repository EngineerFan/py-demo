# author  : Ryan
# datetime: 2020/9/24 18:32
# software: PyCharm

"""
description: 144. 二叉树的前序遍历


给定一个二叉树，返回它的 前序 遍历。

 示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,2,3]

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from typing import List


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        resultList = list()
        if root is None:
            return resultList
        q = list()
        q.append(root)
        while len(q) != 0:
            tempNode = q[0]
            q.pop(0)
            resultList.append(tempNode.val)
            if tempNode.left:
                q.insert(0, tempNode.left)
            if tempNode.right:
                if tempNode.left is None:
                    q.insert(0, tempNode.right)
                else:
                    q.insert(1, tempNode.right)
        return resultList
