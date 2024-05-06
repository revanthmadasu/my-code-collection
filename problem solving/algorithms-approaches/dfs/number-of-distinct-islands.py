'''
    Problem: https://leetcode.com/problems/number-of-distinct-islands/
    Concepts: DFS, Matrix, Backtracking
    performance: 64.12% runtime, 52.20% memory
'''
from typing import List
class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        visited = [[False for c in range(len(grid[0]))] for r in range(len(grid))]
        def dfs(r, c, poss):
            if not visited[r][c]:
                poss.append((r,c))
            visited[r][c] = True
            if r+1 < len(grid) and (not visited[r+1][c]) and grid[r+1][c] == 1:
                dfs(r+1, c, poss)
            if r-1 >= 0 and (not visited[r-1][c]) and grid[r-1][c] == 1:
                dfs(r-1, c, poss)
            if c+1 < len(grid[0]) and (not visited[r][c+1]) and grid[r][c+1] == 1:
                dfs(r, c+1, poss)
            if c-1 >= 0 and (not visited[r][c-1]) and grid[r][c-1] == 1:
                dfs(r, c-1, poss)
        distinctIslands = set()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1 and not visited[r][c]:
                    positions = []
                    dfs(r,c,positions)
                    positions.sort(key=lambda pos: (pos[0], pos[1]))
                    minR = min(position[0] for position in positions)
                    minC = min(position[1] for position in positions)
                    distinctIslands.add(tuple([(position[0]-minR, position[1]-minC) for position in positions]))
        return len(distinctIslands)