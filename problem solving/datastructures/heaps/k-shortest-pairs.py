'''
    problem: https://leetcode.com/problems/find-k-pairs-with-smallest-sums/
    concepts: heaps
    performance: 81.08% runtime, 69.68% memory
'''
import heapq
from typing import List

class Solution:
        def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
            heap = []
            heapq.heapify(heap)
            visited = set()
            n1 = len(nums1)
            n2 = len(nums2)
            res = []
            c = 0
            p1 = 0
            p2 = 0
            heapq.heappush(heap, (nums1[p1]+nums2[p2], p1, p2))
            visited.add((p1, p2))
            while c < k and len(heap):
                # print(f'cur heap: {heap}')
                next_min_pair = heapq.heappop(heap)
                p1 = next_min_pair[1]
                p2 = next_min_pair[2]
                res.append([nums1[p1], nums2[p2]])
                c += 1

                if p1+1 < n1 and not((p1+1, p2) in visited):
                    heapq.heappush(heap, (nums1[p1+1]+nums2[p2], p1+1, p2))
                    visited.add((p1+1, p2))
                if p2+1 < n2 and not((p1, p2+1) in visited):
                    heapq.heappush(heap, (nums1[p1]+nums2[p2+1], p1, p2+1))
                    visited.add((p1, p2+1))
            return res