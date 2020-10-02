# author  : Ryan
# datetime: 2020/10/1 12:02
# software: PyCharm

"""
description: 剑指 Offer 32 - II. 从上到下打印二叉树 II

从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。

 

例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [9,20],
  [15,7]
]
 

提示：

节点总数 <= 1000

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from typing import List


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        q = [root]
        resultList = [[root.val]]
        levelNodeList = []
        while True:
            if len(q) == 0:
                length = len(levelNodeList)
                if length == 0:
                    break
                tempList = []
                for i in range(length):
                    tempList.append(levelNodeList[i].val)
                    q.append(levelNodeList[i])
                resultList.append(tempList)
                levelNodeList.clear()
            else:
                node = q.pop(0)
                if node.left:
                    levelNodeList.append(node.left)
                if node.right:
                    levelNodeList.append(node.right)
