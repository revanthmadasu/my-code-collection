'''
    Problem: https://leetcode.com/problems/longest-consecutive-sequence
    Concepts: Sets, Recursion, Memoization, Union find, DFS
    performance: 5% runtime, 5% memory
'''
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums_set = set(nums)
        @lru_cache(maxsize=None)
        def getLowerCount(n):
            if n-1 in nums_set:
                return 1 + getLowerCount(n-1)
            return 1
        _max = 1
        for num in nums:
            _max = max(_max, getLowerCount(num))
        return _max
