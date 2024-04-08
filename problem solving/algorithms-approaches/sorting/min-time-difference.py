
'''
    problem: https://leetcode.com/problems/minimum-time-difference
    concepts: Array, Sorting
    performance: 98.95% runtime, 39.85% memory
'''
from typing import List
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timeVals = []
        for timePoint in timePoints:
            hrs, mins = timePoint.split(':')
            timeVals.append(int(hrs)*60+int(mins))
        timeVals.sort()
        minTimeDiff = float('inf')
        for i in range(0, len(timeVals)):
            if i+1 < len(timeVals):
                minTimeDiff = min(timeVals[i+1]-timeVals[i], minTimeDiff)
            else:
                minTimeDiff = min(timeVals[0]+1440-timeVals[i], minTimeDiff)
        return minTimeDiff