'''
    problem: https://leetcode.com/problems/prison-cells-after-n-days/
    concepts: Hashtable
    performance: 50.46% runtime, 33.49% memory
'''
from typing import List
class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        cellsMap = dict()
        cycle = None
        
        # Simulate the days until a cycle is detected or n days are completed
        for i in range(n):
            next_day = [0] * len(cells)
            for j in range(1, len(cells) - 1):
                if cells[j - 1] == cells[j + 1]:
                    next_day[j] = 1
                else:
                    next_day[j] = 0
            
            if tuple(next_day) in cellsMap:
                cycle = i - cellsMap[tuple(next_day)]
                break
            
            cellsMap[tuple(next_day)] = i
            cells = next_day
        
        # If a cycle is detected, skip days by modulo operation
        if cycle:
            n %= cycle
            
            for i in range(n):
                next_day = [0] * len(cells)
                for j in range(1, len(cells) - 1):
                    if cells[j - 1] == cells[j + 1]:
                        next_day[j] = 1
                    else:
                        next_day[j] = 0
                cells = next_day
        
        return cells