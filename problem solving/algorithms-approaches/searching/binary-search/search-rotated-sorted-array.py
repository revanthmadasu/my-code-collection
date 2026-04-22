'''
    problem: https://leetcode.com/problems/search-in-rotated-sorted-array/
    concepts: binary search, searching, array
    performance: 100% runtime, 43.48% memory
'''
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while right - left > 1:
            # print(f'searching in {nums[left:right+1]}')
            mid = (left+right) // 2
            if nums[mid] == target:
                return mid
            if (
                (target > nums[right] and nums[mid] > nums[right] and target < nums[mid]) or 
                (target > nums[right] and nums[mid] < nums[right]) or 
                (target < nums[mid] and nums[mid] < nums[right])
                ):
            # if (target > nums[mid] and target > nums[right]) or (target < nums[mid] and (target > nums[left] or nums[mid] )):
                right = mid-1
            else:
                left = mid + 1
        # print(f'out of binary search - searching in {nums[left:right+1]}')
        if target not in [nums[left], nums[right]]:
            return -1
        if nums[left] == target:
            return left
        return right
                    