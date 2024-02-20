'''
    problem: https://leetcode.com/problems/find-peak-element/
    concepts: 
    performance: 89.63% runtime, 93.05% memory
'''
from typing import List
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        m = max(nums)
        return nums.index(m)
