'''
    problem: https://leetcode.com/problems/path-with-maximum-gold
    concepts: DFS, Recursion, Backtracking, Matrix, Array
    performance: 90.74% runtime, 31.94% memory
'''
from typing import List
class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def dfs(pos):
            r, c = pos
            visited[r][c] = True
            maxRes = 0
            if r-1 >= 0 and not visited[r-1][c] and grid[r-1][c] != 0:
                maxRes = max(dfs((r-1, c)), maxRes)
            if c-1 >= 0 and not visited[r][c-1] and grid[r][c-1] != 0:
                maxRes = max(dfs((r, c-1)), maxRes)
            if r+1 < len(grid) and not visited[r+1][c] and grid[r+1][c] != 0:
                maxRes = max(dfs((r+1, c)), maxRes)
            if c+1 < len(grid[0]) and not visited[r][c+1] and grid[r][c+1] != 0:
                maxRes = max(dfs((r, c+1)), maxRes)
            visited[r][c] = False
            return maxRes + grid[r][c]
        maxRes = 0
        visited = [[False] * len(grid[1]) for r in range(len(grid))]
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                maxRes = max(maxRes, dfs((r,c)))
        return maxRes