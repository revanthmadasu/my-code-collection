'''
    problem: https://leetcode.com/problems/shortest-distance-from-all-buildings/
    concepts: BFS, Matrix, Queue
    performance: 17.18% runtime, 30.97% memory
'''
from typing import List
from collections import deque
class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        buildings = set()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    buildings.add((r,c))
        m, n = len(grid), len(grid[0])
        landsStatus = dict()
        def addBuildingAccessToLand(landPos, buildingCost):
            if landPos not in landsStatus:
                landsStatus[landPos] = 0, 0
            buildingCount, cost = landsStatus[landPos]
            landsStatus[landPos] = (buildingCount + 1, cost + buildingCost)
        def provideAccessToLands(r, c):
            visited = set()
            curR, curC = r, c
            # visited.add((curR, curC))
            q = deque()
            q.append(((curR, curC), 0))
            while q:
                pos, dist = q.popleft()
                # if pos in visited:
                #     continue
                visited.add(pos)
                for r_ch, c_ch in [(-1,0), (0,1), (1,0), (0,-1)]:
                    nextR = pos[0] + r_ch
                    nextC = pos[1] + c_ch
                    if nextR >= 0 and nextR < m and nextC >= 0 and nextC < n and (nextR, nextC) not in visited and grid[nextR][nextC] == 0:
                        addBuildingAccessToLand((nextR, nextC), dist + 1)    
                        visited.add((nextR, nextC))
                        
                        q.append(((nextR, nextC), dist+1))
            
        for building in buildings:
            r, c = building
            provideAccessToLands(r, c)  
        # print(f'buildings: {buildings}')
        # print(f'buildings: {len(buildings)}')
        
        # print(f'lands status: {landsStatus}')
        availableLands = [landsStatus[landStatus][1] for landStatus in landsStatus if landsStatus[landStatus][0] == len(buildings)]
        # print(f'availableLands: {availableLands}, {[landStatus[0] for landStatus in landsStatus]}')
        if len(availableLands):
            return min(availableLands)
        else:
            return -1