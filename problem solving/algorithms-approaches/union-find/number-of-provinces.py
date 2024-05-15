'''
    Problem: https://leetcode.com/problems/number-of-provinces
    Concepts: Union find, Matrix
    performance: 30.32% runtime, 61.92% memory
'''
from typing import List
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        roots = [i for i in range(n)]
        def find(searchItem):
            while roots[searchItem] != searchItem:
                roots[searchItem] = roots[roots[searchItem]]
                searchItem = roots[searchItem]
            return searchItem
        def union(item1, item2):
            par1 = find(item1)
            par2 = find(item2)
            if par1 != par2:
                roots[par2] = par1
        for r in range(n):
            for c in range(r+1, n):
                if isConnected[r][c] == 1:
                    union(r,c)
        res = set()
        for i in range(n):
            res.add(find(i))
        return len(res)