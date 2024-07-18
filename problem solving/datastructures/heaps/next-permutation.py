'''
    problem: https://leetcode.com/problems/next-permutation/
    concepts: Heap, Min Heap, Max Heap
    performance: 71.05% runtime, 6.39 memory
'''
from typing import List
from heapq import heappush, heappop
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return nums
        maxHeap = [-nums[-1]]
        minHeap = []
        for i in range(len(nums)-2, -1, -1):
            if (-maxHeap[0]) > nums[i]:
                while maxHeap and (-maxHeap[0]) > nums[i]:
                    heappush(minHeap, -heappop(maxHeap))
                curNum = nums[i]
                nums[i] = heappop(minHeap)
                while minHeap:
                    heappush(maxHeap, -heappop(minHeap))
                heappush(maxHeap, -curNum)
                break
            else:
                heappush(maxHeap, -nums[i])

        i = len(nums)-1
        while maxHeap:
            nums[i] = -heappop(maxHeap)
            i -= 1

        