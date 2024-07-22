'''
    problem: https://leetcode.com/problems/sparse-matrix-multiplication
    concepts: Matrix
    performance: 20.86% runtime, 46.61% memory
'''
from typing import List
class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        # rows in mat1 == cols in mat2
        prodMat = [[1] * len(mat2[0]) for _ in range(len(mat1))]
        # print(f'prodMat: {prodMat}')
        for r in range(len(prodMat)):
            for c in range(len(prodMat[0])):
                _sum = 0
                for i in range(len(mat1[0])):
                    _sum += (mat1[r][i] * mat2[i][c])
                prodMat[r][c] = _sum
        return prodMat