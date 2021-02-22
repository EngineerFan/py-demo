# author  : Ryan
# datetime: 2020/9/25 8:49
# software: PyCharm

"""
description: 110. 平衡二叉树

给定一个二叉树，判断它是否是高度平衡的二叉树。

本题中，一棵高度平衡二叉树定义为：

一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。

示例 1:

给定二叉树 [3,9,20,null,null,15,7]

    3
   / \
  9  20
    /  \
   15   7
返回 true 。

示例 2:

给定二叉树 [1,2,2,3,3,null,null,4,4]

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
返回 false 。

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from typing import List


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def dfs(startNode: TreeNode, depth: List[int]) -> int:
            if startNode is None:
                return depth[0]
            if not startNode.left and not startNode.right:
                return depth[0]
            depth[0] = depth[0] + 1
            print('rChild Val: ', depth[0])
            dfs(startNode.left, depth)
            dfs(startNode.right, depth)
            return depth[0]

        if root is None:
            return True
        q = [root]
        while len(q) != 0:
            node = q.pop(0)
            lNode, rNode = None, None
            if node.left:
                q.append(node.left)
                lNode = node.left
            if node.right:
                q.append(node.right)
                rNode = node.right
            if lNode or rNode:
                # print(lNode , rNode.val)
                lInitDepth, rInitDepth = [0], [0]
                if lNode:
                    lNodeDepth = dfs(lNode, lInitDepth) + 1
                else:
                    lNodeDepth = 0
                if rNode:
                    rNodeDepth = dfs(rNode, rInitDepth) + 1
                else:
                    rNodeDepth = 0
                print(lNodeDepth, rNodeDepth)
                if abs(lNodeDepth - rNodeDepth) > 1:
                    return False
        return True
