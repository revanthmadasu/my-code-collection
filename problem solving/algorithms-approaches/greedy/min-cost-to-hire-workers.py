'''
    problem: https://leetcode.com/problems/minimum-cost-to-hire-k-workers/
    concepts: Greedy, Heap, Max Heap, Sorting
    performance: 71.89% runtime, 36.17% memory
    #explanation: https://www.youtube.com/watch?v=f879mUH6vJk&t=102s
    #revise
'''
from typing import List
import math
from heapq import heappush, heappop
class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        res = math.inf
        rateQualityPair = [(wage[i]/quality[i], quality[i])for i in range(len(quality))]
        rateQualityPair.sort(key=lambda p: p[0])
        totalQuality = 0
        maxHeap = []
        for rate, q in rateQualityPair:
            heappush(maxHeap, -q)
            totalQuality += q
            if len(maxHeap) > k:
                totalQuality += heappop(maxHeap)
            if len(maxHeap) == k:
                res = min(res, totalQuality * rate)
        return res
                