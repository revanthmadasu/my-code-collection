'''
    problem: https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/
    concepts: Array
    performance: 50% runtime, 100% memory
'''
from typing import List
class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)

        curI = 0
        longestLen = 1
        while curI < len(nums) - 1:
            if nums[curI] < nums[curI + 1]:
                start = curI
                while curI < len(nums) - 1 and nums[curI] < nums[curI + 1]:
                    curI += 1
                longestLen = max(curI - start + 1, longestLen)
            elif nums[curI] > nums[curI + 1]:
                start = curI
                while curI < len(nums) - 1 and nums[curI] > nums[curI + 1]:
                    curI += 1
                longestLen = max(curI - start + 1, longestLen)
            else:
                curI += 1
        return longestLen