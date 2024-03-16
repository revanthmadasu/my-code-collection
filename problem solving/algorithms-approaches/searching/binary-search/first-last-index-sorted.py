'''
    problem: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array
    concepts: binary search
    performance: 75.54% runtime, 85.36% memory
'''
from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # iterative binary search - high performance
        def binarySearch(start, end):
            while end-start != 0:
                mid = (start+end)//2
                if nums[mid] > target:
                    end = max(mid-1, start)
                elif nums[mid] == target:
                    return mid
                else:
                    start = min(mid+1, end)
            if end-start == 0:
                return end if nums[end] == target else -1
        # recursive binary search - lower performance
        # def binarySearch(start, end):
        #     while end-start != 0:
        #         mid = (start+end)//2
        #         if nums[mid] > target:
        #             end = max(mid-1, start)
        #         elif nums[mid] == target:
        #             return mid
        #         else:
        #             start = min(mid+1, end)
        #     if end-start == 0:
        #         return end if nums[end] == target else -1

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
