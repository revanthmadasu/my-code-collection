'''
URL: https://leetcode.com/problems/max-area-of-island/
Concept: DFS
Runtime: 164ms => 37.4/100
Memory: 16.5MB => 58.37/100
'''
from collections import defaultdict
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.visitedMap = defaultdict(lambda: False)
        self.m = len(grid)
        self.n = len(grid[0])
        self.grid = grid
        max_area = 0
        for i in range(self.m):
            for j in range(self.n):
                cell = grid[i][j]
                if cell == 1 and not self.visitedMap[self.getKey(i,j)]:
                        area = self.getArea(i,j)
                        max_area = area if area > max_area else max_area
        return max_area
    def getArea(self,i,j):
        area = 1
        self.visitedMap[self.getKey(i,j)] = True
        if i+1 < self.m and self.grid[i+1][j] == 1 and not self.visitedMap[self.getKey(i+1,j)]:
            print(f'classic comb B1: ({i+1}, {j})')
            area += self.getArea(i+1,j)
        if i-1 >= 0 and self.grid[i-1][j] == 1 and not self.visitedMap[self.getKey(i-1,j)]:
            print(f'classic comb B2: ({i-1}, {j})')
            area += self.getArea(i-1,j)
        if j+1 < self.n and self.grid[i][j+1] == 1 and not self.visitedMap[self.getKey(i,j+1)]:
            print(f'classic comb B3: ({i}, {j+1})')
            area += self.getArea(i,j+1)
        if j-1 >= 0 and self.grid[i][j-1] == 1 and not self.visitedMap[self.getKey(i,j-1)]:
            print(f'classic comb B4: ({i}, {j-1})')
            area += self.getArea(i,j-1)
        return area
    def getKey(self,i,j):
        return f'{i}x{j}'