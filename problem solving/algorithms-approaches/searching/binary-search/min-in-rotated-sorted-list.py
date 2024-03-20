'''
    problem: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array
    concepts: binary search, searching
    performance: 48.77% runtime, 23.17% memory
'''
from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] < nums[len(nums)-1] or len(nums) <= 2:
            return min(nums)
        start = 0
        end = len(nums) - 1
        while end - start > 1:
            mid = (start+end)//2
            if nums[mid] < nums[end] and nums[mid] > nums[start] and nums[mid-1] > nums[mid] and nums[mid+1] > nums[mid]:
                return nums[mid]
            if nums[mid] > nums[end]:
                start = mid
            elif nums[mid] < nums[start]:
                end = mid
            if start == end:
                return nums[start]
            elif end - start == 1:
                return min(nums[start], nums[end])
        return -1        
