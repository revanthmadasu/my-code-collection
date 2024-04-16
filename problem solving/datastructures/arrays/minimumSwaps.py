'''
    problem: https://leetcode.com/problems/minimum-adjacent-swaps-to-make-a-valid-array/
    concepts: Array
    performance: 56.74% runtime, 5.61% memory
'''
from typing import List
class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        maxNumI = len(nums)-1
        minNumI = 0
        for i in range(len(nums)):
            if nums[len(nums)-1-i] > nums[maxNumI]:
                maxNumI = len(nums)-1-i
            if nums[i] < nums[minNumI]:
                minNumI = i
        return len(nums)-1 - maxNumI + minNumI - int(minNumI > maxNumI)
