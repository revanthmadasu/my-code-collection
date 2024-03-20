'''
    problem: https://leetcode.com/problems/maximal-square
    concepts: dynamic programming, multi dimensional DP
    performance: 35.59% runtime, 25.07% memory
'''
from typing import List
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dpGrid = []
        for i in range(len(matrix)):
            row = []
            for j in range(len(matrix[0])):
                row.append(int(matrix[i][j]))
            row.append(0)
            dpGrid.append(row)
        dpGrid.append([0] * (len(matrix[0]) + 1))
        maxArea = 0
        for r in range(len(matrix)-1, -1, -1):
            for c in range(len(matrix[0])-1, -1, -1):
                if dpGrid[r][c] != 0:
                    dpGrid[r][c] += min(dpGrid[r][c+1], dpGrid[r+1][c], dpGrid[r+1][c+1])
                    maxArea = max(maxArea, dpGrid[r][c])
        # print(dpGrid)
        return maxArea*maxArea
