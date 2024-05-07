from typing import List
class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        nodes = {iN: set() for iN in range(n)}
        sources = set([i for i in range(n)])
        for edge in edges:
            nodes[edge[1]].add(edge[0])
            if edge[0] in sources:
                sources.remove(edge[0])
        visited = dict()
        def dfs(node):
            if node in visited:
                return visited[node]
            res = set()
            for nextNode in nodes[node]:
                res = res.union(dfs(nextNode))
                res.add(nextNode)
            visited[node] = res
            return res
        for node in sources:
            dfs(node)
        return [sorted(list(visited[node])) for node in range(n)]
