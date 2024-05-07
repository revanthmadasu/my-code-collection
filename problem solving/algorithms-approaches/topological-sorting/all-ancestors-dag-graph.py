'''
    Problem: https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/
    Concepts: Topological Sort, Graph, DFS
    performance: 56.46% runtime, 11.96% memory
    #todo: improve memory
'''
from typing import List
class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        nodes = {iN: set() for iN in range(n)}
        sources = set([i for i in range(n)])
        for edge in edges:
            nodes[edge[1]].add(edge[0])
            if edge[0] in sources:
                sources.remove(edge[0])
        @cache
        def dfs(node):
            res = set()
            for nextNode in nodes[node]:
                res = res.union(dfs(nextNode))
                res.add(nextNode)
            return res
        for node in sources:
            dfs(node)
        return [sorted(list(dfs(node))) for node in range(n)]
