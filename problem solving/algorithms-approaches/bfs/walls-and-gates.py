'''
    Problem: https://leetcode.com/problems/walls-and-gates/
    Concepts: BFS, Matrix, Queue
    performance: 83.18% runtime, 43.43% memory
'''
from collections import deque
from typing import List
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        q = deque()
        m = len(rooms)
        n = len(rooms[0])
        for r in range(m):
            for c in range(n):
                if rooms[r][c] == 0:
                    q.append(((r,c), 0))
        while q:
            pos, dist = q.popleft()
            for nextPos in [(0,1), (1,0), (0,-1), (-1,0)]:
                r,c = pos[0] + nextPos[0], pos[1] + nextPos[1]
                if r < m and r >= 0 and c < n and c >= 0 and rooms[r][c] > 0:
                    if rooms[r][c] > dist + 1:
                        rooms[r][c] = dist + 1
                        q.append(((r,c), dist+1))
