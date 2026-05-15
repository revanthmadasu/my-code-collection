'''
    Problem: https://leetcode.com/problems/longest-consecutive-sequence
    Concepts: Sets, Recursion, Memoization, Union find, DFS
    performance: 5% runtime, 5% memory
'''
from functools import lru_cache
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        @lru_cache
        def getPrevSubsequentCount(num):
            return (1 + getPrevSubsequentCount(num-1)) if num in numsSet else 0
        _max = 0
        for num in numsSet:
            _max = max(getPrevSubsequentCount(num), _max)
        return _max