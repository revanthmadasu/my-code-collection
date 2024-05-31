'''
    problem: https://leetcode.com/problems/single-number-iii/
    concepts: Sets
    performance: 89.89% runtime, 41.53% memory
'''
from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        nums_set = set()
        for num in nums:
            nums_set.remove(num) if num in nums_set else nums_set.add(num)
        return list(nums_set)