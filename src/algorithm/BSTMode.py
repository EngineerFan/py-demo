# author  : Ryan
# datetime: 2020/9/2 16:47
# software: PyCharm

"""
description: 501. 二叉搜索树中的众数

给定一个有相同值的二叉搜索树（BST），找出 BST 中的所有众数（出现频率最高的元素）。

假定 BST 有如下定义：

结点左子树中所含结点的值小于等于当前结点的值
结点右子树中所含结点的值大于等于当前结点的值
左子树和右子树都是二叉搜索树
例如：
给定 BST [1,null,2,2],

   1
    \
     2
    /
   2
返回[2].

提示：如果众数超过1个，不需考虑输出顺序

进阶：你可以不使用额外的空间吗？（假设由递归产生的隐式调用栈的开销不被计算在内）

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from typing import List


class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        resultList = []
        resultElementList = []
        resultCountList = []
        if root is None:
            return resultList
        def dfs(root: TreeNode, resultList: List[int]) -> None:
            if root is None:
                return
            resultList.append(root.val)
            dfs(root.left, resultList)
            dfs(root.right, resultList)
        dfs(root, resultList)
        resultList.sort(reverse=False)
        for i in range(len(resultList)):
            if i != 0 and resultList[i] == resultList[i - 1]:
                continue
            resultCountList.append(resultList.count(resultList[i]))
            resultElementList.append(resultList[i])
        target = max(resultCountList)
        result = []
        for i in range(len(resultCountList)):
            if target == resultCountList[i]:
                result.append(resultElementList[i])

        return result
