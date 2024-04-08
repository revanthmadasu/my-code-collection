'''
    problem: https://leetcode.com/problems/random-pick-with-weight
    concepts: Prefix Sum, Binary Search, Searching, Random, Math
    performance: 98.95% runtime, 39.85% memory
'''
import random
from typing import List
class Solution:

    def __init__(self, w: List[int]):
        self.weights = w
        self.n = len(w)
        self.prefixSum = []
        _sum = 0
        for wi in w:
            _sum += wi
            self.prefixSum.append(_sum)

    def pickIndex(self) -> int:
        randomNumber = self.prefixSum[-1] * random.random()
        left = 0
        right = self.n-1
        while left < right:
            mid = (left+right) // 2
            if self.prefixSum[mid] < randomNumber:
                left = mid + 1
            else:
                right = mid
        return left

    # time limit exceeded - 0(n) complexity
    # def __init__(self, w: List[int]):
    #     self.weights = w
    #     self.n = len(w)
    #     weightsSum = sum(w)
    #     self.probs = [wi/weightsSum for wi in w]
    #     self.pickCounts = [0] * len(w)
    #     self.totalPickCount = 0

    # def pickIndex(self) -> int:
    #     maxI = 0
    #     def getPDiff(i):
    #         p = self.probs[i]
    #         curFrac = self.pickCounts[i]/max(self.totalPickCount, 1)
    #         return p - curFrac
    #     for i in range(self.n):
    #         if getPDiff(i) > getPDiff(maxI):
    #             maxI = i
    #     self.totalPickCount += 1
    #     self.pickCounts[maxI] += 1
    #     return maxI


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()