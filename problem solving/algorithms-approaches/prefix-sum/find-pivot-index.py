'''
    Problem: https://leetcode.com/problems/find-pivot-index
    Concepts: Prefix Sum
    performance: 34.19% runtime, 11.93% memory
'''
from typing import List
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefixSum = []
        for num in nums:
            prefixSum.append((prefixSum[-1] if len(prefixSum) else 0)+num)
        # print(f'prefix sum is {prefixSum}')
        for i in range(len(nums)):
            leftSum = prefixSum[i] - nums[i]
            rightSum = prefixSum[-1] - prefixSum[i]
            if leftSum == rightSum:
                return i
        return -1