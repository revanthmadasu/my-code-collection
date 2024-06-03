'''
    problem: https://leetcode.com/problems/search-in-rotated-sorted-array/
    concepts: binary search, searching, array
    performance: 80.95% runtime, 89.48% memory
    #todo: write clean code
'''
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)-1
        while start < end:
            # print(f'searching between {start} - {end}')
            mid = (start + end) // 2
            isRotated = nums[start] > nums[end]
            midRotated = nums[start] > nums[mid]
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                if isRotated:
                    if midRotated:
                        if nums[end] >= target:
                            start = mid+1
                        else:
                            end = mid-1
                    else:
                        start = mid+1
                else:
                    start = mid+1
            elif target < nums[mid]:
                if isRotated:
                    if midRotated:
                        end = mid-1
                    else:
                        if target >= nums[start]:
                            end = mid-1
                        else:
                            start = mid+1
                else:
                    end = mid - 1
        if target == nums[start]:
            return start
        elif target == nums[end]:
            return end
        else:
            return -1
                    