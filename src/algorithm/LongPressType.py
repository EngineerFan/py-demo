# author  : Ryan
# datetime: 2020/10/21 20:15
# software: PyCharm

"""
description: 925. 长按键入

你的朋友正在使用键盘输入他的名字 name。偶尔，在键入字符 c 时，按键可能会被长按，而字符可能被输入 1 次或多次。

你将会检查键盘输入的字符 typed。如果它对应的可能是你的朋友的名字（其中一些字符可能被长按），那么就返回 True。

 

示例 1：

输入：name = "alex", typed = "aaleex"
输出：true
解释：'alex' 中的 'a' 和 'e' 被长按。
示例 2：

输入：name = "saeed", typed = "ssaaedd"
输出：false
解释：'e' 一定需要被键入两次，但在 typed 的输出中不是这样。
示例 3：

输入：name = "leelee", typed = "lleeelee"
输出：true
示例 4：

输入：name = "laiden", typed = "laiden"
输出：true
解释：长按名字中的字符并不是必要的。

"""


class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        typedList = list(typed)
        originList = list(name)
        typedLength, originLength = len(typedList), len(originList)
        originCount, typedCount = 1, 0
        index, i = 0, 0
        haveFinished = False
        while i < originLength:
            originElement = originList[i]
            while i + 1 < originLength and originElement == originList[i + 1]:
                i = i + 1
                originCount += 1
            for j in range(index, typedLength):
                if originElement == typedList[j]:
                    typedCount += 1
                    if j + 1 >= typedLength:
                        haveFinished = True
                else:
                    if typedCount >= originCount:
                        index = j
                        typedCount = 0
                        break
                    else:
                        return False
            if haveFinished:
                if typedCount >= originCount and originLength - 1 - i > 0:
                    return False
            originCount = 1
            i = i + 1
        if index < typedLength and typedList[index] != originList[i - 1]:
            return False
        return True


if __name__ == '__main__':
    so = Solution()
    name = "alex"
    typed = "alexxr"
    print(so.isLongPressedName(name, typed))
