'''
    Problem: https://leetcode.com/problems/sort-colors/
    Concepts: Arrays, Sorting
    performance: 78.21% runtime, 62.06% memory
'''
from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red, white, blue = 0, 0, 0
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                red += 1
            elif nums[i] == 1:
                white += 1
            else:
                blue += 1
            i += 1
        i = 0
        while i < len(nums):
            if red:
                nums[i] = 0
                red -= 1
            elif white:
                nums[i] = 1
                white -= 1
            else:
                nums[i] = 2
                blue -= 1
            i += 1
        