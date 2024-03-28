'''
    problem: https://leetcode.com/problems/shortest-distance-to-target-color
    concepts: Dynamic Programming
    performance: 24.76% runtime, 78.10% memory
'''
from typing import List
class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:

        dp = [[-1] * len(colors) for _ in range(3)]
        for i in range(3):
            dp[i][len(colors)-1] = 0 if colors[len(colors)-1] == i+1 else -1
            for j in range(len(colors)-2, -1, -1):
                if colors[j] == i+1:
                    dp[i][j] = 0
                else:
                    if dp[i][j+1] != -1:
                        dp[i][j] = dp[i][j+1] + 1
            # dp[i][0] = 0 if colors[0] == i+1 else -1
            for j in range(1, len(colors)-1):
                if colors[j] == i+1:
                    dp[i][j] = 0
                else:
                    poss = [num for num in [dp[i][j+1], dp[i][j-1]] if num >= 0]
                    if len(poss):
                        dp[i][j] = min(poss) + 1
            if dp[i][len(colors)-2] != -1 and dp[i][len(colors)-1] == -1:
                dp[i][len(colors)-1] = dp[i][len(colors)-2] + 1
        res = []
        for query in queries:
            res.append(dp[query[1]-1][query[0]])
        return res