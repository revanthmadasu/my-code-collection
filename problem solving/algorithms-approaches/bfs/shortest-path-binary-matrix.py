'''
    Problem: https://leetcode.com/problems/shortest-path-in-binary-matrix/
    Concepts: BFS, Matrix, Queue
    performance: 90.37% runtime, 84.50% memory
'''
from collections import deque
from typing import List
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        q = deque()
        q.append(((0,0), 1))
        n = len(grid)
        if n == 1 and grid[0][0] == 0:
            return 1
        grid[0][0] = 2
        while q:
            pos, pathLen = q.popleft()
            nextPoss = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
            for nextPos in nextPoss:
                r,c = pos[0] +nextPos[0], pos[1] + nextPos[1]
                if r < n and c < n and r >= 0 and c >= 0 and grid[r][c] == 0:
                    if (r,c) == (n-1,n-1):
                        return pathLen+1
                    grid[r][c] = 2
                    q.append(((r,c), pathLen+1))
        return -1