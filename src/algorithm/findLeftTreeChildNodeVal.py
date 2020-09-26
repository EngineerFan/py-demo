# author  : Ryan
# datetime: 2020/9/22 13:22
# software: PyCharm

"""
description: 513. 找树左下角的值

给定一个二叉树，在树的最后一行找到最左边的值。

示例 1:

输入:

    2
   / \
  1   3

输出:
1
 

示例 2:

输入:

        1
       / \
      2   3
     /   / \
    4   5   6
       /
      7

输出:
7
 

注意: 您可以假设树（即给定的根节点）不为 NULL。


"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        q = [root]
        levelList = [[root.val]]
        tempList = []
        while True:
            if len(q) == 0:
                tempListLength = len(tempList)
                if tempListLength == 0:
                    break
                newLevelList = []
                for i in range(tempListLength):
                    q.append(tempList[i])
                    newLevelList.append(tempList[i].val)
                levelList.append(newLevelList)
                tempList.clear()
            else:
                tn = q[0]
                q.pop(0)
                if tn.left:
                    tempList.append(tn.left)
                if tn.right:
                    tempList.append(tn.right)
        return levelList[-1][0]
