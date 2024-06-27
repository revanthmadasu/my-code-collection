'''
    Problem: https://leetcode.com/problems/last-stone-weight/
    Concepts: Heap, Min Heap
    performance: 42.64% runtime, 95.27% memory
'''
from heapq import heapify, heappop, heappush
from typing import List
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-stone for stone in stones]
        heapify(maxHeap)
        # print(f'maxHeap: {maxHeap}')
        while len(maxHeap) > 1:
            # print(f'curHeap: {maxHeap}')
            x = -heappop(maxHeap)
            y = -heappop(maxHeap)
            # print(f'x is : {x}, y is {y}')
            if x > y:
                heappush(maxHeap, y-x)
        if len(maxHeap):
            return -maxHeap[0]
        return 0
