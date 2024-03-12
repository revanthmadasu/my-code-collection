'''
    problem: https://leetcode.com/problems/unique-paths-ii
    concepts: dynamic programming
    performance: 64.30% runtime, 58.73% memory
'''
from typing import List
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        pathsGrid = []
        for i in range(m):
            pathsGrid.append([0]*n)
        pathsGrid[0][0] = int(obstacleGrid[0][0] != 1)
        # print(pathsGrid)
        for r in range(m):
            for c in range(n):
                if obstacleGrid[r][c] == 0:
                    if r-1 >= 0:
                        pathsGrid[r][c] += pathsGrid[r-1][c]
                    if c-1 >= 0:
                        pathsGrid[r][c] += pathsGrid[r][c-1]
        # print(pathsGrid)
        return pathsGrid[m-1][n-1]