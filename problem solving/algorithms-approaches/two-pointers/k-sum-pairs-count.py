'''
    Problem: https://leetcode.com/problems/max-number-of-k-sum-pairs/
    Concepts: Dynamic Programming
    performance: 63.70% runtime, 77.56% memory
'''
from typing import List
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        start = 0
        end = len(nums) - 1
        resCount = 0
        while start < end and start < len(nums) and end >= 0:
            _sum = nums[start] + nums[end]
            if _sum == k:
                resCount += 1
                start += 1
                end -= 1
                continue
            elif _sum < k:
                start += 1
            else:
                end -= 1
        return resCount