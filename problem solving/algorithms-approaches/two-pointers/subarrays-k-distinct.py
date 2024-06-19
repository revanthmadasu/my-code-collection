'''
    Problem: https://leetcode.com/problems/subarrays-with-k-different-integers/
    Concepts: Two Pointers, Heap, max heap, hashtable
    performance: 40.43% runtime, 43.92% memory
'''
from collections import deque
from heapq import heappush
from typing import List
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        left = 0
        right = 0
        n = len(nums)
        numsOcc = dict()
        goodCount = 0
        maxHeap = []
        while right < n:
            while len(numsOcc) <= k and right < n:
                if nums[right] not in numsOcc:
                    if len(numsOcc) == k:
                        break
                    numsOcc[nums[right]] = deque()
                    heappush(maxHeap, -right)
                numsOcc[nums[right]].append(right)
                right += 1
            # print(f'right processed till {right}')
            while len(numsOcc) == k and left < n:
                curGoodCount = (right - (-maxHeap[0]))
                goodCount += curGoodCount
                # print(f'removing: leftI: {left}-{nums[left]}, count: {curGoodCount}')
                if len(numsOcc[nums[left]]) > 1:
                    heappush(maxHeap, -numsOcc[nums[left]][1])
                    numsOcc[nums[left]].popleft()
                else:
                    del numsOcc[nums[left]]
                left += 1
        return goodCount
                    
