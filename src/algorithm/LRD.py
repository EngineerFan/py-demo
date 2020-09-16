# author  : Ryan
# datetime: 2020/8/21 8:42
# software: PyCharm

"""
description: 二叉搜索树的后序遍历序列

输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。如果是则返回 true，否则返回 false。假设输入的数组的任意两个数字都互不相同。

 

参考以下这颗二叉搜索树：

     5
    / \
   2   6
  / \
 1   3
示例 1：

输入: [1,6,3,2,5]
输出: false
示例 2：

输入: [1,3,2,6,5]
输出: true
 

提示：

数组长度 <= 1000


"""
from typing import List


class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:

        def traverse(postorder: List[int], left: int, right: int):
            if left >= right:
                return True
            mid = left
            root = postorder[right]
            while postorder[mid] < root:
                mid += 1
            temp = mid
            while temp < right:
                if postorder[temp] < root:
                    return False
                temp += 1
            return traverse(postorder, left, mid - 1) and traverse(postorder, mid, right - 1)

        return traverse(postorder, 0, len(postorder) - 1)


if __name__ == '__main__':
    so = Solution()
    postorder = [1, 6, 3, 2, 5]
    print(so.verifyPostorder(postorder))
