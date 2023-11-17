'''
    Problem: https://leetcode.com/problems/number-of-islands
    Concepts: matrix, disjointset, union-find
    performance: 5.10% runtime, 7.74% memory
    todo: improve performance
'''
from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        disjoint_set = DisjointSet()
        m = len(grid) # m rows
        n = len(grid[0]) # n rows
        def getVal(row, col):
            return str(row).zfill(3)+str(col).zfill(3)
        for i in range(m):
            for j in range(n):
                cur_block = grid[i][j]
                if cur_block == "0":
                    continue
                disjoint_set.makeSet(getVal(i, j))
                if i > 0 and grid[i-1][j] == "1":
                    disjoint_set.union(getVal(i-1, j), getVal(i, j))
                if j > 0 and grid[i][j-1] == "1":
                    disjoint_set.union(getVal(i, j-1), getVal(i, j))
        print(disjoint_set.getAllSets())
        return len(disjoint_set.getAllSets())

class DisjointSet:
    def __init__(self):
        self.valuesSetMap = defaultdict(lambda: None)
        self.allSets = []
    def makeSet(self, val):
        self.valuesSetMap[val] = set([val])
        self.allSets.append(self.valuesSetMap[val])
    def findSet(self, value):
        return self.valuesSetMap[value]
    def union(self, val1, val2):
        valSet1 = self.valuesSetMap[val1]
        valSet2 = self.valuesSetMap[val2]
        merged = valSet1.union(valSet2)
        if valSet1 in self.allSets:
            self.allSets.remove(valSet1)
        if valSet2 and (valSet2 in self.allSets): 
            self.allSets.remove(valSet2)
        self.allSets.append(merged)
        for val in merged:
            self.valuesSetMap[val] = merged
    def getAllSets(self):
        return self.allSets