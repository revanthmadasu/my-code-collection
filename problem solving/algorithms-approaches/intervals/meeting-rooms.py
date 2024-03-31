'''
    Problem: https://leetcode.com/problems/meeting-rooms/
    Concepts: Interval
    performance: 85.04% runtime, 17.74% memory
'''
from typing import List
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        for i in range(len(intervals)-1):
            firstInterval = intervals[i]
            secondInterval = intervals[i+1]
            if firstInterval[0] <= secondInterval[0] and secondInterval[0] < firstInterval[1]:
                return False
        return True