'''
    Problem: https://leetcode.com/problems/pacific-atlantic-water-flow/
    Concepts: BFS, Graph
    performance: 46.19% runtime, 53.41% memory
'''
from typing import List
from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        def bfs(q):
            visited = set()
            possible = [[False] * n for _ in range(m)]
            while q:
                cPos = q.popleft()
                if (cPos[0], cPos[1]) in visited:
                    continue
                visited.add((cPos[0], cPos[1]))
                possible[cPos[0]][cPos[1]] = True
                for nextPos in [(cPos[0]+1, cPos[1]),(cPos[0], cPos[1]+1),(cPos[0]-1, cPos[1]), (cPos[0], cPos[1]-1)]:
                    if nextPos[0] < m and nextPos[0] >= 0 and nextPos[1] < n and nextPos[1] >= 0:
                        if nextPos not in visited and heights[nextPos[0]][nextPos[1]] >= heights[cPos[0]][cPos[1]]:
                            q.append(nextPos)
            return possible
        pacificQ = deque()
        atlanticQ = deque()
        for r in range(m):
            pacificQ.append((r, 0))
            atlanticQ.append((r, n-1))
        for c in range(n):
            pacificQ.append((0, c))
            atlanticQ.append((m-1, c))
        # print(f'pacific q: {pacificQ}')
        # print(f'atlantic q: {atlanticQ}')
        pacificPossible = bfs(pacificQ)
        atlanticPossible = bfs(atlanticQ)
        res = []
        for r in range(m):
            for c in range(n):
                if pacificPossible[r][c] and atlanticPossible[r][c]:
                    res.append([r,c])
        return res