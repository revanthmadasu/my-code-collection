'''
    Problem: https://leetcode.com/problems/longest-increasing-path-in-a-matrix/description/
    Concepts: Dynamic Programming, Memoization
    performance: 60.88% runtime, 29.76% memory
'''
from typing import List
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        @lru_cache(None)
        def dp(r,c):
            # print(f'new call {(r,c)}')
            maxLen = 0
            for pos in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                if pos[0] < len(matrix) and pos[0] >= 0 and pos[1] < len(matrix[0]) and pos[1] >= 0:
                    # print(pos)
                    if matrix[pos[0]][pos[1]] > matrix[r][c]:
                        maxLen = max(dp(pos[0], pos[1]), maxLen)
            return maxLen + 1
        maxLen = 1
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                maxLen = max(dp(r, c), maxLen)
        return maxLen