'''
[[1,4],[2,10],[4,5]]

[[-18,16],[92,93],[46,56],[67,79],[59,60],[33,41],[-67,-49]]

'''
from typing import List
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        intervals.sort(key=lambda x: x[1])  # Sort intervals by end times
        count = 0
        prev_end = intervals[0][1]
        
        for i in range(1, len(intervals)):
            if intervals[i][0] < prev_end:  # If current interval overlaps with previous
                count += 1  # Increment count
            else:
                prev_end = intervals[i][1]  # Update previous end time
        
        return count