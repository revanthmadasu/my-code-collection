'''
    Problem: https://leetcode.com/problems/kth-largest-element-in-a-stream/
    Concepts: Heap, Min Heap
    performance: 65.59% runtime, 48.10% memory
'''
from heapq import heappush, heappop, heappushpop
from typing import List
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap = []
        self.k = k
        for num in nums:
            heappush(self.minHeap, num)
        while len(self.minHeap) > k:
            heappop(self.minHeap)

    def add(self, val: int) -> int:
        # print(f'adding {val}, minHeap: {self.minHeap}, maxHeap: {self.maxHeap}')
        if len(self.minHeap) < self.k:
            heappush(self.minHeap, val)
        else:
            heappushpop(self.minHeap,val)
        return self.minHeap[0]