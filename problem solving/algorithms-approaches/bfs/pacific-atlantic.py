'''
    Problem: https://leetcode.com/problems/pacific-atlantic-water-flow/
    Concepts: BFS, Graph
    performance: 56.65% runtime, 82.25% memory
'''
from collections import deque
from typing import List
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        def bfs(pos, visited):
            queue = deque()
            queue.append(pos)
            while len(queue):
                pos = queue.popleft()
                if pos in visited:
                    continue
                r,c = pos
                visited.add(pos)
                nextPos = [nP for nP in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)] if nP[0] < m and nP[0] >= 0 and nP[1] < n and nP[1] >= 0 and nP not in visited and heights[r][c] <= heights[nP[0]][nP[1]] and nP not in visited]
                queue.extend(nextPos)
        pacificVisited = set()
        atlanticVisited = set()
        pacificPoints = []
        atlanticPoints = []
        for c in range(n):
            pacificPoints.append((0, c))
            atlanticPoints.append((m-1, c))
        for r in range(m):
            pacificPoints.append((r, 0))
            atlanticPoints.append((r, n-1))
        for pacPoint in pacificPoints:
            bfs(pacPoint, pacificVisited)
        for atlPoint in atlanticPoints:
            bfs(atlPoint, atlanticVisited)

        bothVisited = pacificVisited & atlanticVisited
        return [list(pos)for pos in bothVisited]
