'''
    Problem: https://leetcode.com/problems/meeting-rooms-ii/
    Concepts: Interval
    performance: 25.31% runtime, 55.93% memory
'''
'''
0-10 15-20, 25-30

0-10 0-15 11-15 11-17 12-14 15-18
[[11,20],[4,19],[13,17],[6,13]]
[4,19],[6,13],[11,20],[13,17]
[[4,18],[1,35],[12,45],[25,46],[22,27]] -> [1,35],[4,18],[12,45],[22,27],[25,46] [36, 50]
[1,4,12,22,25,36]
[18,27,35,45,46,50]
'''
from typing import List

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        starts = [interval[0] for interval in intervals]
        ends = [interval[1] for interval in intervals]
        starts.sort()
        ends.sort()
        startI = 0
        endI = 0
        count = 0
        maxCount = 0
        while startI < len(intervals):
            while startI < len(intervals) and starts[startI] < ends[endI]:
                count += 1
                startI += 1
            maxCount = max(maxCount, count) 
            while endI < len(intervals) and startI < len(intervals) and starts[startI] >= ends[endI]:
                count -= 1
                endI += 1
        return maxCount
