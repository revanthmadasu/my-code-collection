'''
    Problem: https://leetcode.com/problems/longest-continuous-increasing-subsequence
    Concepts: Arrays
    performance: 85.47% runtime, 39.98% memory
'''
'''
sols = [1,1,1,1,1]
nums = [1,3,5,4,7]
1,2,3,1,2
'''
from typing import List
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        _max = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                dp[i] += dp[i-1]
                _max = max(_max, dp[i])
        return _max
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        _max = 1
        curCount = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                curCount += 1
                _max = max(_max, curCount)
            else:
                curCount = 1
        return _max