'''
    problem: https://leetcode.com/problems/longest-common-subsequence/
    concepts: dynamic programming, Multidimensional DP
    performance: 23.83% runtime, 79.68% memory
'''
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0] * (len(text2)+1) for _ in range(len(text1)+1)]
        for r in range(len(text1)-1, -1, -1):
            for c in range(len(text2)-1, -1, -1):
                dp[r][c] = max((dp[r+1][c+1] + int(text1[r] == text2[c]), dp[r][c+1], dp[r+1][c]))
        # print(dp)
        return dp[0][0]
# class Solution:
#     def longestCommonSubsequence(self, text1: str, text2: str) -> int:
#         dp = [[0 for j in range(len(text2)+1)]for i in range(len(text1)+1)]
#         for r in range(len(text1)-1, -1, -1):
#             for c in range(len(text2)-1, -1, -1):
#                 if text1[r] == text2[c]:
#                     dp[r][c] = 1 + dp[r+1][c+1]
#                 else:
#                     dp[r][c] = max(dp[r+1][c], dp[r][c+1])
#         return dp[0][0]