class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        len1, len2 = len(text1), len(text2)

        dp = [[0 for _ in range(len2 + 1)] for _ in range(len1 + 1)]

        for i in range(len1 - 1, -1, -1):
            for j in range(len2 - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])

        return dp[0][0]


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]
        for row in range(1, len(text1) + 1):
            for col in range(1, len(text2) + 1):
                dp[row][col] = max(
                    dp[row - 1][col],
                    dp[row][col - 1],
                    dp[row - 1][col - 1] + int(text1[row - 1] == text2[col - 1]),
                )

        return dp[-1][-1]
