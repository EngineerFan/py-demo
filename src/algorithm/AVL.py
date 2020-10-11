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
        if root is None:
            return True
        q = [root]

        def dfs(startNode: TreeNode, height: List[int], maxVal: List[int]) -> None:
            if not startNode:
                maxVal[0] = max(maxVal[0], height[0])
                return
            height[0] = height[0] + 1
            dfs(startNode.left, height, maxVal)
            print('maxVal: ', maxVal)
            dfs(startNode.right, height, maxVal)

        while len(q) != 0:
            tempNode = q[0]
            q.pop(0)
            if tempNode.left:
                q.append(tempNode.left)
            if tempNode.right:
                q.append(tempNode.right)
            # 递归分别求高度
            lHeight, rHeight, maxVal = [0], [0], [0]
            dfs(tempNode.left, lHeight, maxVal)
            lHeight[0], maxVal[0] = maxVal[0], 0
            dfs(tempNode.right, rHeight, maxVal)
            rHeight[0] = maxVal[0]
            if abs(lHeight[0] - rHeight[0]) > 1:
                return False
        return True
