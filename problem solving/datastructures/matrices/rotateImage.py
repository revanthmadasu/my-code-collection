'''
    problem: https://leetcode.com/problems/rotate-image
    concepts: matrices
    performance: 87.50% runtime, 25.03% memory
'''
from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for level in range(n//2):
            start = level
            end = n - level - 1 # inclusive
            for i in range(end-start):
                # print(f'{start, start+i} -> {start+i, end} -> {end,end-i} -> {end-i,start} -> {start, start+i}')
                matrix[start][start+i], matrix[start+i][end], matrix[end][end-i], matrix[end-i][start] = matrix[end-i][start], matrix[start][start+i], matrix[start+i][end], matrix[end][end-i]
        return matrix