'''
    problem: https://leetcode.com/problems/the-maze-ii/
    concepts: Graph, Dijkstra
    performance: 9.29% runtime, 5.39% memory
    #todo: improve performance - try bfs instead of dijkstra
'''
from typing import List
from heapq import heappop, heappush
class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        wallNeighbours = set()
        m = len(maze)
        n = len(maze[0])
        for r in range(len(maze)):
            for c in range(len(maze[0])):
                if (r-1 < 0 or maze[r-1][c] == 1) or (c-1 < 0 or maze[r][c-1] == 1) or (c+1 >= n or maze[r][c+1] == 1) or (r+1 >= m or maze[r+1][c] == 1):
                    if maze[r][c] != 1:
                        wallNeighbours.add((r,c))
        visited = set()
        nodesMap = dict()
        def addNode(node1, node2, dist):
            if node1 not in nodesMap:
                nodesMap[node1] = dict()
            if node2 not in nodesMap:
                nodesMap[node2] = dict()
            nodesMap[node1][node2] = dist
            # nodesMap[node2][node1] = dist
        wallNeighbours.add((start[0], start[1]))
        for neigh in wallNeighbours:
            r,c = neigh
            # print(f'checking for {(r,c)}')
            lr = r
            while lr >= 0 and maze[lr][c] != 1:
                lr -= 1
            lr += 1
            hr = r
            while hr < m and maze[hr][c] != 1:
                hr += 1
            hr -= 1
            lc = c
            while lc >= 0 and maze[r][lc] != 1:
                lc -= 1
            lc += 1
            hc = c
            while hc < n and maze[r][hc] != 1:
                hc += 1
            hc -= 1
            if r - lr > 0:
                addNode((r,c), (lr,c), r-lr)
            if hr - r > 0:
                addNode((r,c), (hr,c), hr-r)
            if c - lc > 0:
                addNode((r,c), (r,lc), c-lc)
            if hc - c > 0:
                addNode((r,c), (r,hc), hc-c)
            if hr - lr > 0:
                addNode((hr,c), (lr,c), hr-lr)
                addNode((lr,c), (hr,c), hr-lr)
            if hc - lc > 0:
                addNode((r,hc), (r,lc), hc-lc)
                addNode((r,lc), (r,hc), hc-lc)

            addNode((r,c), (r,c), 0)
            # print(f'neighs: {(r, lc)}, {(r, hc)}, {(hr, c)}, {(lr, c)}')
            
        if (destination[0], destination[1]) not in nodesMap:
            return -1
        # find shortest distances using dijksta algorithm
        visited = set()
        # q = deque()
        sourceNode = nodesMap[(start[0], start[1])]
        # q.append((start[0], start[1]))
        minHeap = [(0, (start[0], start[1]))]
        while minHeap:
            dist, visitingNode = heappop(minHeap)
            # visitingNode = q.popleft()
            # print(f'visiting node is {visitingNode}')
            if visitingNode in visited:
                continue
            visited.add(visitingNode)
            neighs = list(nodesMap[visitingNode].keys())
            for neigh in neighs:
                # print(f'sn is {sourceNode}, neigh is {neigh}')
                # print(f'{sourceNode[(neigh[0], neigh[1])]}')
                sourceNode[(neigh[0], neigh[1])] = min(sourceNode[neigh] if neigh in sourceNode else float('inf'), sourceNode[visitingNode] + nodesMap[visitingNode][neigh])
                if neigh not in visited:
                    heappush(minHeap, ((sourceNode[(neigh[0], neigh[1])], neigh)))
                    # q.append(neigh)
            # print(f'after adding {visitingNode} - {sourceNode}')
        # print(sourceNode)
        if (destination[0], destination[1]) not in sourceNode:
            return -1
        # print(sourceNode)
        return sourceNode[(destination[0], destination[1])]
            