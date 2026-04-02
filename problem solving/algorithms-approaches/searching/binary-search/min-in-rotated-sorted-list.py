'''
    problem: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array
    concepts: binary search, searching
    performance: 48.77% runtime, 23.17% memory
'''
from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1        
        while left < right:
            if nums[left] < nums[right]:
                return nums[left]
            mid = (left + right)//2
            if nums[mid] < nums[left]:
                right = mid
            else:
                left = mid + 1
        return min(nums[left], nums[right])
