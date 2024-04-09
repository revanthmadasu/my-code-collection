'''
    problem: https://leetcode.com/problems/swim-in-rising-water/
    concepts: Heap
    performance: 93.84% runtime, 42.98% memory
'''
from typing import List
import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        minHeap = [(grid[0][0], (0,0))]
        heapq.heapify(minHeap)
        visited = set((0,0))
        maxTimeReq = grid[0][0]
        while minHeap:
            timeReq, pos = heapq.heappop(minHeap) 
            maxTimeReq = max(maxTimeReq, timeReq)
            if pos[0] == len(grid)-1 and pos[1] == len(grid[0])-1:
                return maxTimeReq
            for nextPos in [(pos[0]+1, pos[1]), (pos[0], pos[1]+1), (pos[0]-1, pos[1]), (pos[0], pos[1]-1)]:
                if nextPos[0] >= 0 and nextPos[0] < len(grid) and nextPos[1] >= 0 and nextPos[1] < len(grid[0]):
                    if nextPos not in visited:
                        heapq.heappush(minHeap, (grid[nextPos[0]][nextPos[1]], nextPos))
                        visited.add(nextPos)
        return -1
