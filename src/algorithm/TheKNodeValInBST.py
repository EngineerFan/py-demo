# author  : Ryan
# datetime: 2020/10/1 16:21
# software: PyCharm

"""
description: 剑指 Offer 54. 二叉搜索树的第k大节点

给定一棵二叉搜索树，请找出其中第k大的节点。

 

示例 1:

输入: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
输出: 4
示例 2:

输入: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
输出: 4
 

限制：

1 ≤ k ≤ 二叉搜索树元素个数

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from typing import List


class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        nodeList = []

        def dfs(root: TreeNode, nodeList: List[int]) -> None:
            if not root:
                return
            nodeList.append(root.val)
            if root.left:
                dfs(root.left, nodeList)
            if root.right:
                dfs(root.right, nodeList)

        dfs(root, nodeList)
        nodeList.sort()
        return nodeList[len(nodeList) - k]
