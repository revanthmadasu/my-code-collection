'''
    problem: https://leetcode.com/problems/target-sum
    concepts: Dynamic Programming, 0/1 Knapsack, DP Cache
    performance: 72.96% runtime, 26.34% memory
'''
from typing import List
from functools import cache
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @cache
        def dp(i, acc):
            if i+1 >= len(nums):
                return int(acc+nums[i] == target) + int(acc-nums[i] == target)
            pos = dp(i+1, acc+nums[i])
            neg = dp(i+1, acc-nums[i])
            return pos + neg
        # without dp - pure recursive solution
        # def recursiveSol(i, acc):
        #     acc1 = acc + nums[i]
        #     acc2 = acc - nums[i]
        #     if i+1 < len(nums):
        #         recursiveSol(i+1, acc1)
        #         recursiveSol(i+1, acc2)
        #     else:
        #         if acc1 == target:
        #             res += 1
        #         if acc2 == target:
        #             res += 1
        return dp(0,0)

