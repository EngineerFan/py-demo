# author  : Ryan
# datetime: 2020/8/28 16:27
# software: PyCharm

"""
description:  102. 二叉树的层序遍历

给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。

 

示例：
二叉树：[3,9,20,null,null,15,7],

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

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from typing import List

import queue


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []
        if root is None:
            return result
        q = queue.Queue()
        q.put(root)
        levelNodeList = []
        result.append([root.val])
        while not q.empty():
            node = q.get_nowait()
            if node.left:
                levelNodeList.append(node.left)
            if node.right:
                levelNodeList.append(node.left)
            if q.empty():
                if len(levelNodeList) == 0:
                    return result
                tempLevelList = []
                for i in range(len(levelNodeList)):
                    q.put(levelNodeList[i])
                    tempLevelList.append(levelNodeList[i].val)
                levelNodeList.clear()
                result.append(tempLevelList)
            else:
                continue

        return result
