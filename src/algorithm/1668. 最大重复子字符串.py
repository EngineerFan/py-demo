'''
给你一个字符串 sequence ，如果字符串 word 连续重复 k 次形成的字符串是 sequence 的一个子字符串，那么单词 word 的 重复值为 k 。单词 word 的 最大重复值 是单词 word 在 sequence 中最大的重复值。如果 word 不是 sequence 的子串，那么重复值 k 为 0 。

给你一个字符串 sequence 和 word ，请你返回 最大重复值 k





'''


class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        for i in range(len(sequence)):
            maxResult = max(self.js(sequence, word, i), maxResult)
        return maxResult

    def js(self, sequence: str, word: str, i: int) -> int:
        result = maxResult = 0
        while i < len(sequence):
            start, end = i, i + len(word)
            if end <= len(sequence) and word == sequence[i:end]:
                print(i, end, sequence[i:end])
                result += 1
                i = end
            else:
                maxResult = max(maxResult, result)
                result = 0
                i += 1
        return maxResult


if __name__ == '__main__':
    so = Solution()
    print(so.maxRepeating(sequence='aaabaaaabaaabaaaabaaaabaaaabaaaaba', word='aaaba'))
