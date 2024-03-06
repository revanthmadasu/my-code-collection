'''
    problem: https://leetcode.com/problems/triangle
    concepts: dynamic programming, multi dimensional dynamic programming, arrays
    performance: 68.79% runtime, 85.82% memory
'''
from typing import List
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = triangle[0]
        n = len(triangle)
        for row_i in range(1, n):
            new_dp = []
            # print(f'{row_i} row')
            for col_i in range(row_i+1):
                _min = float('inf')
                if col_i < row_i:
                    _min = min(_min, dp[col_i])
                if col_i -1 >= 0:
                    _min = min(_min, dp[col_i - 1])
                # print(f'selecting {_min}')
                new_dp.append(_min + triangle[row_i][col_i])
            dp = new_dp
        return min(dp)