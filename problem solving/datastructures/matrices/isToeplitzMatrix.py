'''
    problem: https://leetcode.com/problems/toeplitz-matrix/
    concepts: Matrix, Arrays
    performance: 14.95% runtime, 84.74% memory
'''
from typing import List
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        ends = []
        for c in range(n):
            ends.append((m-1, c))
        for r in range(m-2, -1, -1):
            ends.append((r, n-1))
        def isDiagnalSame(pos):
            r,c = pos
            curR, curC = r, c
            while curR >= 0 and curC >= 0:
                if matrix[curR][curC] != matrix[r][c]:
                    return False
                curR -= 1
                curC -= 1
            return True
        for end in ends:
            if not isDiagnalSame(end):
                return False
        return True