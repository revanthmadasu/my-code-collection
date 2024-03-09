'''
    problem: https://leetcode.com/problems/single-number
    concepts: bit manipulation, xor
    performance: 34.83% runtime, 78.07% memory
'''
from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res = res ^ num
        return res