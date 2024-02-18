'''
    problem: https://leetcode.com/problems/maximum-subarray
    concepts: kadane, array
    performance: 92.36% runtime, 68.29% memory
'''
from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum = 0
        max_sum = float('-inf')
        for num in nums:
            if cur_sum + num > 0:
                cur_sum += num
                if cur_sum > max_sum:
                    max_sum = cur_sum
            else:
                cur_sum = 0
                if num > max_sum:
                    max_sum = num
        return max_sum
        