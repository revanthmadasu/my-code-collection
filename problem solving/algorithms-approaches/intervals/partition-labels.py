'''
    problem: https://leetcode.com/problems/partition-labels
    concepts: String, Intervals
    performance: 53.36% runtime, 5.78% memory
'''
from typing import List
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        charIntervals = dict()
        for i in range(len(s)):
            ch = s[i]
            if ch not in charIntervals:
                charIntervals[ch] = (i,i)
            charIntervals[ch] = (charIntervals[ch][0], i)
        intervals = []
        for ch in charIntervals:
            intervals.append(charIntervals[ch])
        intervals.sort(key=lambda interval: interval[0])
        mergedIntervals = [intervals[0]]
        for i in range(1,len(intervals)):
            if intervals[i][0] <= mergedIntervals[-1][1]:
                prevInterval = mergedIntervals.pop()
                mergedIntervals.append((prevInterval[0], max(prevInterval[1], intervals[i][1])))
            else:
                mergedIntervals.append(intervals[i])
        # print(f'all intervals: {intervals}')
        # print(f'merged: {mergedIntervals}')
        return [(interval[1] - interval[0] + 1)for interval in mergedIntervals]