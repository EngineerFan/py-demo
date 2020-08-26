# author  : Ryan
# datetime: 2020/8/26 8:54
# software: PyCharm

"""
description: 两棵二叉搜索树中的所有元素

请你返回一个列表，其中包含 两棵树 中的所有整数并按 升序 排序。.

 

示例 1：



输入：root1 = [2,1,4], root2 = [1,0,3]
输出：[0,1,1,2,3,4]
示例 2：

输入：root1 = [0,-10,10], root2 = [5,1,7,0,2]
输出：[-10,0,0,1,2,5,7,10]
示例 3：

输入：root1 = [], root2 = [5,1,7,0,2]
输出：[0,1,2,5,7]
示例 4：

输入：root1 = [0,-10,10], root2 = []
输出：[-10,0,10]
示例 5：



输入：root1 = [1,null,8], root2 = [8,1]
输出：[1,1,8,8]

"""

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        result = []

        def compareVal(val1: int, val2: int, resultList: List[int]) -> None:
            length = len(resultList)
            if val1 is None and val2 is not None:
                if length != 0:
                    resultList.append(val2)
                    resultList.sort()
                else:
                    resultList.append(val2)

            elif val1 is not None and val2 is None:
                if length != 0:
                    resultList.append(val1)
                    resultList.sort()
                else:
                    resultList.append(val1)
            else:
                if length != 0:
                    resultList.append(val1)
                    resultList.append(val2)
                    resultList.sort()

                else:
                    if val1 <= val2:
                        resultList.append(val1)
                        resultList.append(val2)
                    else:
                        resultList.append(val2)
                        resultList.append(val1)

        def dfs(root1: TreeNode, root2: TreeNode, resultList: List[int]) -> None:
            if root1 is None and root2 is None:
                return
            elif root1 is None and root2 is not None:
                compareVal(None, root2.val, resultList)
                dfs(None, root2.left, resultList)
                dfs(None, root2.right, resultList)
            elif root1 is not None and root2 is None:
                compareVal(root1.val, None, resultList)
                dfs(root1.left, None, resultList)
                dfs(root1.right, None, resultList)
            else:
                if root1.left is None and root1.right is None and root2.left is None and root2.right is None:
                    compareVal(root1.val, root2.val, resultList)
                    return
                else:
                    compareVal(root1.val, root2.val, resultList)
                    dfs(root1.left, root2.left, resultList)
                    dfs(root1.right, root2.right, resultList)

        dfs(root1, root2, result)
        print(result)
        return result
