# author  : Ryan
# datetime: 2020/9/25 12:58
# software: PyCharm

"""
description: 515. 在每个树行中找最大值

您需要在二叉树的每一行中找到最大的值。

示例：

输入:

          1
         / \
        3   2
       / \   \
      5   3   9

输出: [1, 3, 9]


"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import List


class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        resultList = []
        if root is None:
            return resultList
        q = [root]
        tempNodeList = []
        resultList.append(root.val)
        while True:
            if len(q) == 0:
                length = len(tempNodeList)
                if length == 0:
                    break
                maxVal = None
                for i in range(length):
                    q.append(tempNodeList[i])
                    if maxVal is None:
                        maxVal = tempNodeList[i].val
                    maxVal = max(tempNodeList[i].val, maxVal)
                resultList.append(maxVal)
                tempNodeList.clear()
            else:
                tempNode = q[0]
                q.pop(0)
                if tempNode.left:
                    tempNodeList.append(tempNode.left)
                if tempNode.right:
                    tempNodeList.append(tempNode.right)
        return resultList
