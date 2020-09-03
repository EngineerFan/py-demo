# author  : Ryan
# datetime: 2020/9/3 19:45
# software: PyCharm

"""
description: 599. 两个列表的最小索引总和


假设Andy和Doris想在晚餐时选择一家餐厅，并且他们都有一个表示最喜爱餐厅的列表，每个餐厅的名字用字符串表示。

你需要帮助他们用最少的索引和找出他们共同喜爱的餐厅。 如果答案不止一个，则输出所有答案并且不考虑顺序。 你可以假设总是存在一个答案。

示例 1:

输入:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
输出: ["Shogun"]
解释: 他们唯一共同喜爱的餐厅是“Shogun”。
示例 2:

输入:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["KFC", "Shogun", "Burger King"]
输出: ["Shogun"]
解释: 他们共同喜爱且具有最小索引和的餐厅是“Shogun”，它有最小的索引和1(0+1)。

"""
from typing import List


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        if len(list1) == 0 or len(list2) == 0:
            return []
        length1 = len(list1)
        resultIndexList = []
        resultValueList = []
        for i in range(length1):
            try:
                j = list2.index(list1[i])
                print('最小序列： ', [i, j], ' 和为： ', (i + j), ' 对应的餐厅是： ', list1[i])
                resultIndexList.append((i + j))
                resultValueList.append(list1[i])
            except ValueError:
                continue
        minVal = min(resultIndexList)
        result = []
        for i in range(len(resultIndexList)):
            if minVal == resultIndexList[i]:
                result.append(resultValueList[i])
        return result


if __name__ == '__main__':
    so = Solution()
    list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
    list2 = ["KFC", "Shogun", "Burger King"]
    print(so.findRestaurant(list1, list2))
