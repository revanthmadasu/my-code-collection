'''
    Problem: https://leetcode.com/problems/top-k-frequent-elements/
    Concepts: Hash Table, Heap
    performance: 90.23% runtime, 69.78% memory
'''
import heapq
from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsCount = dict()
        for num in nums:
            if num not in numsCount:
                numsCount[num] = 0
            numsCount[num] += 1
        maxHeap = []
        for num in numsCount:
            heapq.heappush(maxHeap, (-numsCount[num], num))
        kNums = []
        for _ in range(k):
            kNums.append(heapq.heappop(maxHeap)[1])
        return kNums