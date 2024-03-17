'''
    problem: https://leetcode.com/problems/set-matrix-zeroes
    concepts: matrices
    performance: 72.77% runtime, 79.15% memory
'''
from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    for k in range(m):
                        if matrix[k][j] != 0:
                            matrix[k][j] = None
                    for k in range(n):
                        if matrix[i][k] != 0:
                            matrix[i][k] = None
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == None:
                    matrix[i][j] = 0