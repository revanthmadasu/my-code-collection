'''
    problem: https://leetcode.com/problems/path-with-maximum-probability/
    concepts: Graph, Dijkstra
    performance: 17.08% runtime, 23.47% memory
'''
from typing import List
from heapq import heappop, heappush
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = dict()
        for i in range(len(edges)):
            u,v = edges[i]
            w = succProb[i]
            if u not in graph:
                graph[u] = dict()
                graph[u][u] = 0
            if v not in graph:
                graph[v] = dict()
                graph[v][v] = 0
            graph[u][v] = w
            graph[v][u] = w
        # print(f'graph: {graph}')
        if start_node not in graph or end_node not in graph:
            return 0
        maxHeap = [(0, start_node)]
        visited = set()

        while maxHeap:
            d, node = heappop(maxHeap)
            d = -d
            if node not in visited:
                visited.add(node)
                for nextNode in graph[node]:
                    nextProb = graph[start_node][node] * graph[node][nextNode]
                    graph[start_node][nextNode] = max(nextProb, graph[start_node][nextNode] if nextNode in graph[start_node] else 0)
                    if nextNode not in visited:
                        heappush(maxHeap, (-graph[start_node][nextNode], nextNode))
        # print(f'after graph: {graph}')
        return graph[start_node][end_node] if end_node in graph[start_node] else 0