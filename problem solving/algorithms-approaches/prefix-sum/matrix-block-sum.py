'''
    Problem: https://leetcode.com/problems/matrix-block-sum
    Concepts: Prefix Sum, Matrix, Array
    performance: 29.66 runtime, 23.09 memory
'''
from typing import List
'''
[
[1,2,3,4],
[4,5,6,7],
[7,8,9,10],
[11,12,13,14]
]

rowsum = [3,6,9,7]
[
[1,3,6,10]
[4,9,15,22]
[7,15,24,34]
[11,23,36,40]
]
]
colsums = [5,7]
'''
class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        ans = [[0] * n for _ in range(m)]
        prefix = []
        for r in range(m):
            _sum = 0
            row = []
            for c in range(n):
                _sum += mat[r][c]
                row.append(_sum)
            prefix.append(row)
                
        for r in range(m):
            for c in range(n):
                _sum = 0
                for i in range(max(r-k, 0), min(r+k+1, m)): 
                    leftMost = 0 if c-k-1 < 0 else prefix[i][c-k-1]
                    rightMost = prefix[i][min(c+k, n-1)]
                    _sum += (rightMost-leftMost)
                ans[r][c] = _sum
                rowsRange = [r-k, r+k]
        # for r in range(m):
        #     for c in range(n):
        #         for i in range(r-k, r+k+1):
        #             for j in range(c-k, c+k+1):
        #                 if i >= 0 and i < m and j >= 0 and j < n:
        #                     ans[r][c] += mat[i][j]
        return ans