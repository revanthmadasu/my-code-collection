'''
    problem: https://leetcode.com/problems/ipo
    concepts: heap, two heap
    performance: 9.43% runtime, 10.79% memory
'''
import heapq
from typing import List
# 2 heap approach
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        eligibleProjectIndices = list(range(len(profits)))
        maxProfitHeap = []
        minCapitalHeap = []
        heapq.heapify(minCapitalHeap)
        heapq.heapify(maxProfitHeap)
        for i in range(len(capital)):
            heapq.heappush(minCapitalHeap, (capital[i], i))
        while len(minCapitalHeap) and minCapitalHeap[0][0] <= w:
            cap, i = heapq.heappop(minCapitalHeap)
            heapq.heappush(maxProfitHeap, (-profits[i], i))

        for _ in range(k):
            if len(maxProfitHeap):
                p_profit ,i = heapq.heappop(maxProfitHeap)
                # print(f'selecting {p_profit}, {i}')
                w += (profits[i])
            while len(minCapitalHeap) and minCapitalHeap[0][0] <= w:
                cap, i = heapq.heappop(minCapitalHeap)
                heapq.heappush(maxProfitHeap, (-profits[i], i))
        return w


# test cases failing
# class Solution:
#     def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
#         eligibleProjectIndices = set(range(len(profits)))
#         maxProfitHeap = []
#         heapq.heapify(maxProfitHeap)
#         totalProfit = w
#         for i in list(eligibleProjectIndices):
#             if capital[i] <= w:
#                 eligibleProjectIndices.remove(i)
#                 heapq.heappush(maxProfitHeap, (-profits[i], i))
#         for _ in range(k):
#             if len(maxProfitHeap):
#                 p_profit ,i = heapq.heappop(maxProfitHeap)
#                 # print(f'selecting {p_profit}, {i}')
#                 w += (profits[i])
#                 totalProfit += profits[i]
#             for i in list(eligibleProjectIndices):
#                 if capital[i] <= w:
#                     eligibleProjectIndices.remove(i)
#                     heapq.heappush(maxProfitHeap, (-profits[i], i))
#         return totalProfit
