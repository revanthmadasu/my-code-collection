'''
    problem: https://leetcode.com/problems/longest-common-subsequence/
    concepts: dynamic programming, Multidimensional DP
    performance: 70.63% runtime, 43.35% memory
'''
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0] * (len(word2)+1) for _ in range(len(word1)+1)]
        for i in range(len(word1)):
            dp[i][len(word2)] = len(word1)-i
        for j in range(len(word2)):
            dp[len(word1)][j] = len(word2)-j
        for r in range(len(word1)-1, -1, -1):
            for c in range(len(word2)-1, -1, -1):
                if word1[r] == word2[c]:
                    dp[r][c] = dp[r+1][c+1]
                else:
                    dp[r][c] = 1 + min(dp[r+1][c], dp[r][c+1], dp[r+1][c+1])
        return dp[0][0]