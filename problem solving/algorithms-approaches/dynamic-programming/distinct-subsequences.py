'''
    problem: https://leetcode.com/problems/distinct-subsequences/
    concepts: dynamic programming, Multidimensional DP, LCS Dp pattern, 2D DP, Tabulation DP
    performance: 43.44% runtime, 47.19% memory
'''
'''
    r a b b b i t
r   
a
b       2 1 0 0 0
b   3 3 3 2 1 0 0
i   1 1 1 1 1 1 0
t   1 1 1 1 1 1 1


'''
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(s) < len(t):
            return 0
        elif len(s) == len(t) and s == t:
            return 1
        dp = [[0] * (len(s)+1) for _ in range(len(t)+1)]
        for c in range(len(s)+1):
            dp[len(t)][c] = 1
        # print(dp)
        for r in range(len(t)-1, -1, -1):
            for c in range(len(s)-1, -1, -1):
                # print(f'r is {r}, c is {c}')
                dp[r][c] = (int(t[r] == s[c]) * dp[r+1][c+1]) + dp[r][c+1]
        # print(dp)
        return dp[0][0]