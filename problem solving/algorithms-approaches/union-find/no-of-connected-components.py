'''
    Problem: https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/
    Concepts: Graph, Union Find
    performance: 54.59% runtime, 77.51% memory
'''
from typing import List
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parents = [i for i in range(n)]
        ranks = [1] * n
        def find(v):
            res = v
            while parents[res] != res:
                parents[res] = parents[parents[res]]
                res = parents[res]
            return res
        def union(v1, v2):
            p1, p2 = find(v1), find(v2)
            if ranks[p1] >= ranks[p2]:
                ranks[p1] += ranks[p2]
                parents[p2] = parents[p1]
            else:
                ranks[p2] += ranks[p1]
                parents[p1] = parents[p2]
        for edge in edges:
            union(edge[0], edge[1])
        return len(set([find(v) for v in range(n)]))