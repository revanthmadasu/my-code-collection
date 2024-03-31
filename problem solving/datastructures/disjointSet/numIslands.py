'''
    Problem: https://leetcode.com/problems/number-of-islands
    Concepts: matrix, disjointset, union-find
    performance: 90.73% runtime, 52.04% memory
'''
from typing import List
from collections import deque
# bfs approach
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        curIslandCount = 0     
        dq = deque()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] != "0":
                    curIslandCount += 1
                    # queue = [(r,c)]
                    dq.append((r,c))
                    # print(f'cur {r}, {c}')
                    while dq:
                        curR, curC = dq.pop()
                        # visited[curR][curC] = True
                        if curR-1 >= 0 and grid[curR-1][curC] == "1":
                            dq.append((curR-1, curC))
                        if curC-1 >= 0 and grid[curR][curC-1] == "1":
                            dq.append((curR, curC-1))
                        if curR+1 < len(grid) and grid[curR+1][curC] == "1":
                            dq.append((curR+1, curC))
                        if curC+1 < len(grid[0]) and grid[curR][curC+1] == "1":
                            dq.append((curR, curC+1))
                        grid[curR][curC] = "0"
        return curIslandCount
# union find approach
# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         disjoint_set = DisjointSet()
#         m = len(grid) # m rows
#         n = len(grid[0]) # n rows
#         def getVal(row, col):
#             return str(row).zfill(3)+str(col).zfill(3)
#         for i in range(m):
#             for j in range(n):
#                 cur_block = grid[i][j]
#                 if cur_block == "0":
#                     continue
#                 disjoint_set.makeSet(getVal(i, j))
#                 if i > 0 and grid[i-1][j] == "1":
#                     disjoint_set.union(getVal(i-1, j), getVal(i, j))
#                 if j > 0 and grid[i][j-1] == "1":
#                     disjoint_set.union(getVal(i, j-1), getVal(i, j))
#         print(disjoint_set.getAllSets())
#         return len(disjoint_set.getAllSets())

# class DisjointSet:
#     def __init__(self):
#         self.valuesSetMap = defaultdict(lambda: None)
#         self.allSets = []
#     def makeSet(self, val):
#         self.valuesSetMap[val] = set([val])
#         self.allSets.append(self.valuesSetMap[val])
#     def findSet(self, value):
#         return self.valuesSetMap[value]
#     def union(self, val1, val2):
#         valSet1 = self.valuesSetMap[val1]
#         valSet2 = self.valuesSetMap[val2]
#         merged = valSet1.union(valSet2)
#         if valSet1 in self.allSets:
#             self.allSets.remove(valSet1)
#         if valSet2 and (valSet2 in self.allSets): 
#             self.allSets.remove(valSet2)
#         self.allSets.append(merged)
#         for val in merged:
#             self.valuesSetMap[val] = merged
#     def getAllSets(self):
#         return self.allSets
    
        
        
grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
print(Solution().numIslands(grid))