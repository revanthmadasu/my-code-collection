'''
    problem: https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden
    concepts: Greedy, Dynamic Programming, Intervals
    performance: 50.11% runtime, 35.31% memory
'''
from typing import List
class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        intervals = []
        for i in range(len(ranges)):
            if ranges[i] != 0:
                intervals.append((max(0,i - ranges[i]), min(i + ranges[i]-1, n-1)))
        intervals.sort(key = lambda interval: interval[0])
        maxIntervalIndex = -1 # should be index
        maxRight = -1
        minTaps = 0
        for curPoint in range(n):
            curMaxRight = maxRight
            if maxRight < curPoint:
                while maxIntervalIndex+1 < len(intervals) and intervals[maxIntervalIndex+1][0] <= curPoint:
                    maxIntervalIndex += 1
                    curMaxRight = max(curMaxRight, intervals[maxIntervalIndex][1])
            if curPoint > curMaxRight:
                return -1
            else:
                if curMaxRight > maxRight:
                    minTaps += 1
                    maxRight = curMaxRight
        return minTaps
