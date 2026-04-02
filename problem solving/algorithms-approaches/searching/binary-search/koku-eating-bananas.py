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
        kUpper = max(piles)
        kLower = 1
        kCur = 0
        def getHrsRequiredForK(k):
            hrsCount = 0
            for pile in piles:
                hrsCount += math.ceil(pile/k)
            return hrsCount
        while kLower != kUpper:
            kCur = (kLower + kUpper) // 2
            # print(f'{kLower}, {kUpper}, {kCur}')
            hrs = getHrsRequiredForK(kCur)
            if hrs > h:
                kLower = kCur+1
            else:
                kUpper = kCur
        return kLower
        