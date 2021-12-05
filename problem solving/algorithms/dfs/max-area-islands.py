'''
URL: https://leetcode.com/problems/max-area-of-island/
Concept: DFS
Runtime: 172ms => 31.43/100
Memory: 17MB => 38.66/100
'''
from collections import defaultdict
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visitedMap = defaultdict(lambda: False)
        m = len(grid)
        n = len(grid[0])
        max_area = 0
        for i in range(m):
            for j in range(n):
                cell = grid[i][j]
                if cell == 1 and not visitedMap[self.getKey(i,j)]:
                        area = self.getArea(grid, (m,n), (i,j),visitedMap)
                        max_area = area if area > max_area else max_area
        return max_area
    def getArea(self,grid, dimensions, coordinate, visitedMap):
        i = coordinate[0]
        j = coordinate[1]
        m = dimensions[0]
        n = dimensions[1]
        area = 1
        visitedMap[self.getKey(i,j)] = True
        if i+1 < m and grid[i+1][j] == 1 and not visitedMap[self.getKey(i+1,j)]:
            area += self.getArea(grid, (m,n), (i+1,j), visitedMap)
        if i-1 >= 0 and grid[i-1][j] == 1 and not visitedMap[self.getKey(i-1,j)]:
            area += self.getArea(grid, (m,n), (i-1,j), visitedMap)
        if j+1 < n and grid[i][j+1] == 1 and not visitedMap[self.getKey(i,j+1)]:
            area += self.getArea(grid, (m,n), (i,j+1), visitedMap)
        if j-1 >= 0 and grid[i][j-1] == 1 and not visitedMap[self.getKey(i,j-1)]:
            area += self.getArea(grid, (m,n), (i,j-1), visitedMap)
        return area
    def getKey(self,i,j):
        return f'{i}x{j}'