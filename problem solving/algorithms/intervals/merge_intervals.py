'''
    problem: https://leetcode.com/problems/merge-intervals/
    concepts: intervals, arrays, sorting
    performance: 57.28% runtime, 68.60% memory
'''
from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        if n == 1:
            return intervals
        intervals.sort(key = lambda interval: interval[0])
        merged_intervals = [intervals[0]]
        def doesMatch(interval1, interval2):
            merged = []
            if interval1[0] == interval2[0]:
                if interval1[1] > interval2[1]:
                    merged = [interval1]
                else:
                    merged = [interval2]
            elif interval2[0] <= interval1[1]:
                merged = [[interval1[0], interval1[1] if interval1[1] > interval2[1] else interval2[1]]]
            else:
                merged = [interval1, interval2]
            return merged
        i_m = 0
        for i in range(n):
            merged_res = doesMatch(merged_intervals[i_m], intervals[i])
            if len(merged_res) > 1:
                i_m+=1
                merged_intervals.append(merged_res[1])
            else:
                merged_intervals[i_m] = merged_res[0]
        return merged_intervals