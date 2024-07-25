'''
    Problem: https://leetcode.com/problems/min-cost-to-connect-all-points
    Concepts: Graph, Prims, Minimum Spanning Tree
    performance: 63.57% runtime, 48.28% memory
'''
from typing import List
from heapq import heappop, heappush
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = dict()
        def getDistance(i,j):
            return (abs(points[i][0]-points[j][0]) + abs(points[i][1]-points[j][1]))
        if len(points) == 1:
            return 0
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                if i not in edges:
                    edges[i] = []
                if j not in edges:
                    edges[j] = []
                dist = getDistance(i,j)
                edges[i].append((dist, j))
                edges[j].append((dist, i))
        visited = set()
        visited.add(0)
        minHeap = []
        for edge in edges[0]:
            heappush(minHeap, edge)
        totalDistance = 0
        while len(visited) < len(points):
            dist, point = heappop(minHeap)
            if point not in visited:
                totalDistance += dist
                for edge in edges[point]:
                    if edge[1] not in visited:
                        heappush(minHeap, edge)
            visited.add(point)
        return totalDistance