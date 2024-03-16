'''
    problem: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array
    concepts: binary search
    performance: 5.97% runtime, 50.62% memory
'''
from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarySearch(start, end):
            if end-start == 0:
                return end if nums[end] == target else -1
            mid = (start+end)//2
            if nums[mid] > target:
                return binarySearch(start, max(mid-1, start))
            elif nums[mid] == target:
                return mid
            else:
                return binarySearch(min(mid+1, end), end)
        if not len(nums):
            return [-1, -1]
        targetIndex = binarySearch(0, len(nums)-1)
        if targetIndex != -1:
            start = targetIndex
            while start >= 0 and nums[start] == target:
                start -= 1
            end = targetIndex
            while end < len(nums) and nums[end] == target:
                end += 1
            return [start+1, end-1]
        return [-1, -1]
