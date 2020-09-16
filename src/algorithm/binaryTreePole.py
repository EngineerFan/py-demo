# author  : Ryan
# datetime: 2020/9/2 15:21
# software: PyCharm

"""
description: 563. 二叉树的坡度


给定一个二叉树，计算整个树的坡度。

一个树的节点的坡度定义即为，该节点左子树的结点之和和右子树结点之和的差的绝对值。空结点的的坡度是0。

整个树的坡度就是其所有节点的坡度之和。



示例：

输入：
         1
       /   \
      2     3
输出：1
解释：
结点 2 的坡度: 0
结点 3 的坡度: 0
结点 1 的坡度: |2-3| = 1
树的坡度 : 0 + 0 + 1 = 1


提示：

任何子树的结点的和不会超过 32 位整数的范围。
坡度的值不会超过 32 位整数的范围。

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findTilt(self, root: TreeNode) -> int:
        if root is None or (root.left is None and root.right is None):
            return 0
        result = [0]

        def dfs(node: TreeNode, result) -> None:
            if node is None:
                return
            if node.left is not None and node.right is not None:
                result[0] += abs(node.left.val - node.right.val)
            elif node.left is None and node.right is not None:
                result[0] += node.right.val
            elif node.left is not None and node.right is None:
                result[0] += node.left.val
            else:
                return
            dfs(node.left, result)
            dfs(node.right, result)

        dfs(root, result)
        return result[0]
