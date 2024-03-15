'''
    problem: https://leetcode.com/problems/search-a-2d-matrix
    concepts: binary search, recursion
    performance: 54.87% runtime, 50.31% memory
'''
from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        all_nums = []
        for nums_ary in matrix:
            all_nums.extend(nums_ary)
        return self.binarySearch(all_nums, target)
    def binarySearch(self, nums, target):
        n = len(nums)
        mid_i = int(n/2)
        if nums[mid_i] == target:
            return True
        if n > 1:
            if nums[mid_i] > target:
                return self.binarySearch(nums[:mid_i], target)
            else:
                return self.binarySearch(nums[mid_i:], target)
        else:
            return False
        