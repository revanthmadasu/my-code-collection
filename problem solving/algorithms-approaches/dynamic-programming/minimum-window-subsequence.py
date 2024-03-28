'''
    problem: https://leetcode.com/problems/minimum-window-subsequence
    concepts: Dynamic Programming, Multi Dimensional DP, Sliding Window
    performance: 20.61% runtime, 13.39% memory 
    #todo - improve performance
'''
'''
s1 -> column wise
s2 -> row wise
abcdedemnopbdxyzxyzxyzdepqr
bcbcdede
bde

  b c d e d e
b 4-1-1-1-1-1
d 4 3 2 3 2-1
e 4 3 2 1 2 1

'''
class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        # if len(s2) > len(s1):
        #     s1, s2 = s2, s1
        dp = [[0] * (len(s1) + 1)for i in range(len(s2)+1)]
        for i in range(len(s1)+1):
            dp[-1][i] = 0
        for i in range(len(s2)):
            dp[i][-1] = float('inf')
        for r in range(len(s2)-1, -1, -1):
            for c in range(len(s1)-1, -1, -1):
                dp[r][c] = 1 + dp[r+int(s1[c] == s2[r])][c+1]
        # print('dp matrix:')
        # print(dp)
        minSize = float('inf')
        index = -1
        for i in range(len(s1)):
            if dp[0][i] < minSize:
                minSize = dp[0][i]
                index = i
        return "" if minSize == float('inf') else s1[index:index+minSize]