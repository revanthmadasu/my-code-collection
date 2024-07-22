'''
    problem: https://leetcode.com/problems/network-delay-time/
    concepts: Graph, Dijkstra
    performance: 30.86% runtime, 27.80% memory
'''
from typing import List
from heapq import heappop, heappush
import math
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = dict()
        for time in times:
            u,v,w = time
            if u not in graph:
                graph[u] = dict()
                graph[u][u] = 0
            if v not in graph:
                graph[v] = dict()
                graph[v][v] = 0
            graph[u][v] = w
            # graph[v][u] = w
        minHeap = [(0, k)]
        visited = set()
        # added.add(k)
        maxDist = -math.inf
        while minHeap:
            d, node = heappop(minHeap)
            if node not in visited:
                visited.add(node)
                # print(f'visiting: {node}')
                for nextNode in graph[node]:
                    # print(f'nextNode from {node} - {nextNode}')
                    # print(f'dist from {k} to {node} : {graph[k][node]}')
                    # print(f'dist from {node} to {nextNode} : {graph[node][nextNode]}')
                    nextDist = d + graph[node][nextNode]
                    graph[k][nextNode] = min(nextDist, graph[k][nextNode] if nextNode in graph[k] else math.inf)
                    # print(f'updated dist: {graph[k][nextNode]}')
                    if nextNode not in visited:
                        heappush(minHeap, (graph[k][nextNode], nextNode))
        if len(visited) == n:
            for nextNode in graph[k]:
                maxDist = max(graph[k][nextNode], maxDist)
            return maxDist
        else:
            return -1
                    
                    

