'''
    Problem: https://leetcode.com/problems/missing-ranges
    Concepts: Two Pointers, Intervals, Array
    performance: 88.83 runtime, 60.57 memory
'''
from typing import List
class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        p1 = lower # number
        curNumI = 0 # index of nums
        missingIntervals = []
        while p1 <= upper and curNumI < len(nums):
            if p1 == nums[curNumI]:
                p1 += 1
                curNumI += 1
            else:
                missingIntervals.append([p1, nums[curNumI]-1])
                p1 = nums[curNumI]
        if p1 <= upper:
            missingIntervals.append([p1, upper])
        return missingIntervals