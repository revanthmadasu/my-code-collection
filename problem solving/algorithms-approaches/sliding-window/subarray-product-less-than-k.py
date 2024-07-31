'''
    problem: https://leetcode.com/problems/subarray-product-less-than-k/
    concepts: Sliding Window
    performance: 5.02% runtime, 50.04% memory 
'''
from typing import List
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k == 0 or k == 1:
            return 0
        product = nums[0]
        left = 0
        right = 0
        res = 0
        while left <= right and right < len(nums):
            # expand right till maximum
            while right+1 < len(nums) and product*nums[right+1] < k:
                right += 1
                product *= nums[right]
            # even after expansion the window is valid
            # remove lefts till we can add next right
            while right+1 < len(nums) and product*nums[right+1] >= k and left <= right:
                # print(f'b1 adding {left} - {right}')
                if product < k:
                    res += (right-left + 1)
                product /= nums[left]
                left += 1

            if left > right:
                product = nums[left]
                right = left
            if right == len(nums)-1:
                break
            
        if product < k:
            while left <= right:
                res += (right - left + 1)
                left += 1
        return res
