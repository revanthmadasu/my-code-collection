'''
    problem: https://leetcode.com/problems/shuffle-the-array/description/
    Concepts: Array, Two Pointers
    performance: 80.05% runtime, 47.82% memory
'''
from typing import List
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        for i in range(n):
            res.append(nums[i])
            res.append(nums[i+n])
        return res