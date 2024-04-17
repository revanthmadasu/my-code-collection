'''
    problem: https://leetcode.com/problems/rectangle-overlap/
    concepts: Intervals
    performance: 32.11% runtime, 8.64% memory
'''
from typing import List
class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        xIntervals = [(rec1[0], rec1[2]), (rec2[0], rec2[2])]
        yIntervals = [(rec1[1], rec1[3]), (rec2[1], rec2[3])]
        xIntervals.sort()
        yIntervals.sort()
        xIntersecting = (xIntervals[1][0], min(xIntervals[0][1], xIntervals[1][1]))
        yIntersecting = (yIntervals[1][0], min(yIntervals[0][1], yIntervals[1][1]))
        return  xIntersecting[0] < xIntersecting[1] and yIntersecting[0] < yIntersecting[1]
