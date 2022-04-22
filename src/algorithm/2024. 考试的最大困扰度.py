# -*- coding: utf-8 -*-
# @Author      : Ryan
# @Time        : 2022/3/29 19:03
# @Software    : PyCharm
# @Description : 2024. 考试的最大困扰度


class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:

        def countMaxAnswer(ch: str, answerKey: str, k: int) -> int:
            result, left, total = 0, 0, 0
            for right in range(len(answerKey)):
                total += answerKey[right] != ch
                while total > k:
                    total -= answerKey[left] != ch
                    left += 1
                result = max(result, right - left + 1)
            return result

        return max(countMaxAnswer('F', answerKey, k), countMaxAnswer('T', answerKey, k))


if __name__ == '__main__':
    so = Solution()
    print(so.maxConsecutiveAnswers("TTFTTFTT", 1))
