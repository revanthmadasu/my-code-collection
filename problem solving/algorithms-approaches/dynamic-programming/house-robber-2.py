'''
    problem: https://leetcode.com/problems/house-robber-ii
    concepts: dynamic programming, arrays
    performance: 65.56% runtime, 90.71% memory
'''
from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.houseRobber1(nums[1:]), self.houseRobber1(nums[:-1]))
    def houseRobber1(self, nums: List[int]) -> int:
        r1, r2 = 0, 0
        for num in nums:
            temp = max(r1 + num, r2)
            r1, r2 = r2, temp
        return r2