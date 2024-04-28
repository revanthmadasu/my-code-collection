'''
    Problem: https://leetcode.com/problems/sort-integers-by-the-power-value
    Concepts: Sorting, DP, LRU Cache
    performance: 63.67% runtime, 27.01% memory
'''
class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        @lru_cache(maxsize=None)
        def getPowVal(num):
            if num == 1:
                return 1
            return 1 + getPowVal(num/2 if num%2 == 0 else (3*num + 1))
        return sorted(range(lo, hi+1), key=getPowVal)[k-1]
# heap approach
# import heapq
# class Solution:
#     def getKth(self, lo: int, hi: int, k: int) -> int:
#         @lru_cache(maxsize=None)
#         def getPowVal(num):
#             if num == 1:
#                 return 1
#             if num%2 == 0:
#                 return 1 + getPowVal(num/2)
#             else:
#                 return 1 + getPowVal(3*num + 1)
#         minHeap = []
#         heapq.heapify(minHeap)
#         for num in range(lo, hi+1):
#             heapq.heappush(minHeap, (getPowVal(num), num))
#         kthItem = None
#         for i in range(k):
#             kthItem = heapq.heappop(minHeap)
#         return kthItem[1]