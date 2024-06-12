'''
    Problem: https://leetcode.com/problems/contains-duplicate/
    Concepts: Sets
    performance: 99.51% runtime, 81.88% memory
'''
from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numsDict = set()
        for num in nums:
            if num in numsDict:
                return True
            numsDict.add(num)
        return False