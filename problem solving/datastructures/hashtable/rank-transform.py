'''
    problem: https://leetcode.com/problems/rank-transform-of-an-array/
    concepts: Array, Hashtable, Heap
    performance: 13.49% runtime, 69.42% memory
'''
from typing import List
from heapq import heappush, heappop
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        minHeap = []
        for num in arr:
            heappush(minHeap, num)
        ranksDict = dict()
        curRank = 1
        while minHeap:
            num = heappop(minHeap)
            if num not in ranksDict:
                ranksDict[num] = curRank
                curRank += 1
        return [ranksDict[num] for num in arr]