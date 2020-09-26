# author  : Ryan
# datetime: 2020/9/24 13:20
# software: PyCharm

"""
description: 530. 二叉搜索树的最小绝对差

给你一棵所有节点为非负值的二叉搜索树，请你计算树中任意两节点的差的绝对值的最小值。

 

示例：

输入：

   1
    \
     3
    /
   2

输出：
1

解释：
最小绝对差为 1，其中 2 和 1 的差的绝对值为 1（或者 2 和 3）。
 

提示：

树中至少有 2 个节点。

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        treeNodeList = []
        q = [root]
        minVal = -1
        while len(q) != 0:
            tempNode = q[0]
            q.pop(0)
            for i in range(len(treeNodeList)):
                tempVal = abs(tempNode.val - treeNodeList[i])
                if minVal == -1 or tempVal < minVal:
                    minVal = tempVal
            treeNodeList.append(tempNode.val)
            if tempNode.left:
                q.append(tempNode.left)
            if tempNode.right:
                q.append(tempNode.right)
        return minVal
