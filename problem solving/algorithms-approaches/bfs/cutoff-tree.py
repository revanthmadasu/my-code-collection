'''
    problem: https://leetcode.com/problems/cut-off-trees-for-golf-event/
    concepts: BFS, Heap
    #incomplete: time limit exceeded - 33/55 testcases passed
    #todo: complete it - try running multi source shortest path algorithm first to get distances instead of bfs
'''
import heapq
from typing import List
class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        m = len(forest)
        n = len(forest[0])
        minHeap = [] # (height, (i,j))
        heapq.heapify(minHeap)
        for r in range(m):
            for c in range(n):
                if forest[r][c] != 0:
                    heapq.heappush(minHeap, (forest[r][c], (r,c)))
        def getMinDistance(srcPos, dstPos):
            q = [srcPos]
            dist = 0
            visited = dict()
            while q:
                # print(f'cur q: {}')
                newQ = []
                for pos in q:
                    visited[pos] = True
                    if forest[pos[0]][pos[1]] == 0:
                        continue
                    if pos == dstPos:
                        return dist
                    else:
                        nextPos = [(pos[0]+1, pos[1]), (pos[0], pos[1]+1), (pos[0]-1, pos[1]), (pos[0], pos[1]-1)]
                        nextPos = [npos for npos in nextPos if npos[0] >= 0 and npos[0] < m and npos[1] >= 0 and npos[1] < n and npos not in visited]
                        newQ.extend(nextPos)
                q = newQ
                dist += 1
            return -1
        dist = 0
        curPos = (0,0)
        while len(minHeap):
            treeHeight, pos = heapq.heappop(minHeap)
            distToNextPos = getMinDistance(curPos, pos)
            if distToNextPos == -1:
                return -1
            dist += distToNextPos
            curPos = pos
        if len(minHeap):
            return -1
        return dist
