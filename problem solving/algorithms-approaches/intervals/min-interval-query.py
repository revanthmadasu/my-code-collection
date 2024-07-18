'''
    problem: https://leetcode.com/problems/minimum-interval-to-include-each-query/
    concepts: Intervals, Sorting, Heap, Min Heap, Two Pointers
    performance: 60.05% runtime, 26.83% memory
'''
from typing import List
from heapq import heappush, heappop
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key=lambda interval: interval[0])
        originalQueries = queries.copy()
        queries.sort()
        intervalsMinHeap = []
        intervalIndex = 0
        # print(f'queries is {queries}')
        # print(f'intervals is {intervals}')
        res = dict()
        for query in queries:
            if query in res:
                continue
            while intervalIndex < len(intervals) and query >= intervals[intervalIndex][0]:
                heappush(intervalsMinHeap, (intervals[intervalIndex][1] - intervals[intervalIndex][0] + 1, intervalIndex))
                intervalIndex += 1
            while len(intervalsMinHeap) and intervals[intervalsMinHeap[0][1]][1] < query:
                heappop(intervalsMinHeap)
            # print(f'heap for query {query} is {intervalsMinHeap}')
            res[query] = intervalsMinHeap[0][0] if len(intervalsMinHeap) else -1
            # if len(intervalsMinHeap):
            #     res.append(intervalsMinHeap[0][0])
            # else:
            #     res.append(-1)
        return [res[query] for query in originalQueries]