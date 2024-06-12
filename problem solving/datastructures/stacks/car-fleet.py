'''
    Problem: https://leetcode.com/problems/car-fleet/
    Concepts: Stack, Monotonic Stack, Sorting
    performance: 47.41% runtime, 29.30% memory
    #revisit
    #neetcode explanation: https://www.youtube.com/watch?v=Pr6T-3yB9RM
'''
from typing import List
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        cars = []
        for i in range(n):
            time = (target-position[i])/speed[i]
            cars.append((position[i], time))
        cars.sort()
        stack = [cars[-1]]
        for i in range(n-2, -1, -1):
            if not (cars[i][1] <= stack[-1][1]):
                stack.append(cars[i])
        return len(stack)