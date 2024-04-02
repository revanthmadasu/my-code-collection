'''
    Problem: https://leetcode.com/problems/find-the-score-of-all-prefixes-of-an-array/
    Concepts: Array
    performance: 92.72% runtime, 51.90% memory
'''
from typing import List
class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        scores = []
        maxAt = nums[0]
        sumAt = 0
        for i in range(len(nums)):
            maxAt = max(nums[i], maxAt)
            sumAt += nums[i] + maxAt
            scores.append(sumAt)
        return scores
