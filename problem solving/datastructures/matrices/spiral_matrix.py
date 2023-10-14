'''
    problem: https://leetcode.com/problems/spiral-matrix
    concepts: arrays, matrix, loops
    performance: 18.4% runtime, 89.14% memory
    todo: improve runtime
'''
from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ''' 
            m rows, n columns
            direction: right -> down -> left -> up
            right = 0, down = 1, left = 2, up = 3
        '''
        m = len(matrix)
        n = len(matrix[0])

        left = 0
        right = n
        up = 0
        down = m
        res = []
        row = up
        col = left
        while(left < right and up < down):
            # from left to right
            _range = list(range(left, right))
            if not len(_range):
                break
            for i in _range:
                res.append(matrix[up][i])
            up += 1

            # from up to down
            _range = list(range(up, down))
            if not len(_range):
                break
            for i in _range:
                res.append(matrix[i][right - 1])
            right -= 1

            # from right to left
            _range = list(range(right -1, left - 1, -1))
            if not len(_range):
                break
            for i in _range:
                res.append(matrix[down - 1][i])
            down -= 1

            # from down to up
            _range = list(range(down - 1, up - 1, -1))
            if not len(_range):
                break
            for i in _range:
                res.append(matrix[i][left])
            left += 1
        return res
    
sol = Solution()
matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
matrix2 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
matrix3 = [[1,2,3,4,5,6],[7,8,9,10,11,12], [13, 14, 15, 16, 17, 18], [19, 20, 21, 22, 23, 24], [25, 26, 27, 28, 29, 30], [31, 32, 33, 34, 35, 36]]
print(sol.spiralOrder(matrix3))