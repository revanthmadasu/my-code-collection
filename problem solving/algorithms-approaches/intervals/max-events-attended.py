'''
    problem: https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/
    concepts: Intervals, Heap, Minheap, Sorting
    performance: 98.43% runtime, 73.66% memory
'''
import heapq
from typing import List
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort(key=lambda event: event[0])
        started = []
        count = i = 0
        currDay = events[0][0]
        n = len(events)
        while i < n:
            while i < n and events[i][0] == currDay:
                heapq.heappush(started, events[i][1])
                i += 1
            heapq.heappop(started)
            count += 1
            currDay += 1
            while started and started[0] < currDay:
                heappop(started)
            if i < n and not started:
                currDay = events[i][0]
        while started:
            if heappop(started) >= currDay:
                currDay += 1
                count += 1
        return count
# 43/44 testcases passed - timeout
# class Solution:
#     def maxEvents(self, events: List[List[int]]) -> int:
#         # intersections = dict()
#         events.sort(key=lambda event: event[1])
#         segments = []
#         def checkMergeNext(i):
#             if i+1 < len(segments) and segments[i+1][0] <= segments[i][1]+1:
#                 segments[i] = (segments[i][0], segments[i+1][1])
#                 segments.pop(i+1)
#                 return True
#             return False
#         def addSeg(start, end):
#             for i in range(len(segments)):
#                 segment = segments[i]
#                 if segment[0] <= start and start <= segment[1]:
#                     if segment[1]+1 <= end:
#                         # possible
#                         segments[i] = (segment[0], segment[1]+1)
#                         checkMergeNext(i)
#                         return True                        
#                     else:
#                         return False
#                         # not possible
#                 elif segment[0] > start:
#                     segments.insert(i,(start,start))
#                     checkMergeNext(i)
#                     return True
#                 elif segment[1] == start-1:
#                     segments[i] = (segment[0], start)
#                     checkMergeNext(i)
#                     return True
#             segments.append((start, start))
#             return True

#         res = 0
#         for i in range(len(events)):
#             event = events[i]
#             # print(f'seg bf: {segments}')
#             # print(f'checking for event: {event}')
#             if addSeg(event[0], event[1]):
#                 res += 1
#                 # print('possible')
#             # else:
#             #     print(f'not possible')
#             # print(f'seg af: {segments}')
#             # for day in range(event[0], event[1]+1):
#             #     if day not in added:
#             #         # seqEnd[day] = True
#             #         added.add(day)
#             #         break
#         # print(added)
#         # print(segments)
#         return res
#         # return len(added)


