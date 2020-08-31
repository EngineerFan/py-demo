# author  : Ryan
# datetime: 2020/8/28 15:54
# software: PyCharm

"""
description: 104. 二叉树的最大深度


给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明: 叶子节点是指没有子节点的节点。

示例：
给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        depth = 0
        depthList = []

        def dfs(node: TreeNode, depth: int) -> None:
            if node is None:
                depthList.append(depth)
                return
            if node.left is None and node.right is None:
                depth += 1
                depthList.append(depth)
                return
            depth += 1
            dfs(node.left, depth)
            dfs(node.right, depth)

        dfs(root, depth)
        print(depthList)
        return max(depthList)
