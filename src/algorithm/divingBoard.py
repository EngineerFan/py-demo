# author  : Ryan
# datetime: 2020/8/21 15:42
# software: PyCharm

"""
description: 16.11. 跳水板


你正在使用一堆木板建造跳水板。有两种类型的木板，其中长度较短的木板长度为shorter，长度较长的木板长度为longer。你必须正好使用k块木板。编写一个方法，生成跳水板所有可能的长度。

返回的长度需要从小到大排列。

示例 1

输入：
shorter = 1
longer = 2
k = 3
输出： [3,4,5,6]
解释：
可以使用 3 次 shorter，得到结果 3；使用 2 次 shorter 和 1 次 longer，得到结果 4 。以此类推，得到最终结果。
提示：

0 < shorter <= longer
0 <= k <= 100000


"""
from typing import List


class Solution:
    def divingBoard(self, shorter: int, longer: int, k: int) -> List[int]:
        y = 0
        result = []
        if k == 0:
            return result
        if shorter == longer:
            result.append(k * shorter)
            return result
        while y <= k:
            x = k - y
            val = x * shorter + y * longer
            result.append(val)
            y = y + 1
        return result


if __name__ == '__main__':
    so = Solution()
    shorter = 1
    longer = 1
    k = 100000
    print(so.divingBoard(shorter, longer, k))
