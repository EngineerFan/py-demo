class Solution:

    def numTilings(self, n: int) -> int:
        mod = 10 ** 9 + 7
        dp = [[0] * 4 for _ in range(n + 1)]
        dp[0][3] = 1
        for i in range(1, n + 1):
            dp[i][0] = dp[i - 1][3]
            dp[i][1] = (dp[i - 1][0] + dp[i - 1][2]) % mod
            dp[i][2] = (dp[i - 1][0] + dp[i - 1][1]) % mod
            dp[i][3] = (((dp[i - 1][0] + dp[i - 1][1]) % mod + dp[i - 1][2]) % mod + dp[i - 1][3]) % mod
        return dp[n][3]


if __name__ == '__main__':
    so = Solution()
    print(so.numTilings(n=5))
