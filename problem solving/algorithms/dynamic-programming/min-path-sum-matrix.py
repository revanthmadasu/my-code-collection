'''
    problem: https://leetcode.com/problems/minimum-path-sum/
    concepts: dynamic programming
    performance: 78.11% runtime, 39.59% memory
'''
from typing import List
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        minPathGrid = []
        for i in range(m):
            minPathGrid.append([0] * n)
        # minPathGrid[0][0] = grid[0][0]
        for i in range(m):
            for j in range(n):
                prev = None
                if i-1 >= 0:
                    prev = minPathGrid[i-1][j]
                if j-1 >= 0:
                    prev = minPathGrid[i][j-1] if prev == None or prev > minPathGrid[i][j-1] else prev
                minPathGrid[i][j] = grid[i][j] + (prev if prev else 0)
        # print(minPathGrid)
        return minPathGrid[m-1][n-1]
