'''
    problem: https://leetcode.com/problems/partition-equal-subset-sum/
    concepts: dynamic programming, 2D DP, Array, 
    performance: 27.97% runtime, 42.85% memory
'''
from typing import List
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        _sum = sum(nums)
        if _sum%2 != 0:
            return False
        target = int(_sum / 2)
        def coinChange(nums, target):
            # print(f'target is {target}')
            nums.sort(reverse=True)
            dp = [[False] * (target+1) for _ in range(len(nums)+1)]
            for r in range(len(nums)+1):
                dp[r][target] = True
            for r in range(len(nums)-1, -1, -1):
                for curTar in range(1,target+1):
                    col = target - curTar
                    reqTarget = curTar-nums[r]
                    # print(f'col: {col}, curTar: {curTar}, reqTar: {reqTarget}, col index: {target-reqTarget}')
                    dp[r][col] = dp[r+1][col] or (dp[r+1][target-reqTarget] if reqTarget >= 0 else False)
            # print(dp)
            return dp[0][0]
        return coinChange(nums, target)

'''
1,2,3
5
  5 4 3 2 1 0
8
3 T T T T T T
2     T T T T
1         T T

'''