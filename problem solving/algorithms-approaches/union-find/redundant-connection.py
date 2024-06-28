'''
    Problem: https://leetcode.com/problems/redundant-connection
    Concepts: Union find, Graph
    performance: 87.40% runtime, 73.87% memory
'''
from typing import List
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        roots = dict()
        def find(item):
            if item not in roots:
                roots[item] = item
            while roots[item] != item:
                roots[item] = roots[roots[item]]
                item = roots[item]
            return item
        def union(item1, item2):
            root1 = find(item1)
            root2 = find(item2)
            if root1 == root2:
                return False
            else:
                roots[root1] = root2
                return True
        for edge in edges:
            if not union(edge[0], edge[1]):
                return edge
        return None