'''
    Problem: https://leetcode.com/problems/koko-eating-bananas/
    Concepts: Binary Search, Searching
    performance: 5.09% runtime, 42.96% memory
    #todo: improve runtime
'''
from typing import List
import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxPossible = max(piles)
        if h == len(piles):
            return maxPossible
        def isPossible(k):
            curH = 0
            i = 0
            nPiles = piles.copy()
            # print(f'isPossible: {k}')
            while curH < h and i < len(piles):
                # print(f'curH: {curH}, i: {i}, k: {k}')
                nPiles[i]
                curH += math.ceil(nPiles[i]/k)
                i += 1
            return i == len(piles) and curH <= h
        left, right = 1, maxPossible

        while left != right:
            # print(f'left: {left}, right: {right}')
            mid = (left + right) // 2
            if isPossible(mid):
                maxPossible = mid
                right = mid
            else:
                left = mid + 1
        return left
        