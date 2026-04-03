'''
    problem: https://leetcode.com/problems/longest-increasing-subsequence
    concepts: dynamic programming, array
    performance: 8.65% runtime, 67.95% memory
'''
from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        for i in range(n):
            seqs = [dp[x] for x in range(i) if nums[x] < nums[i]]
            dp[i] = dp[i] + (max(seqs) if len(seqs) else 0)
        return max(dp)

    # high performance - 70.48, 95.36
    # def lengthOfLIS(self, arr: List[int]) -> int:
    #     seqCountAry = [1 for i in arr]
    #     n = len(arr)
    #     maxCount = 0
    #     for i in range(n-1, -1, -1):
    #         maxPossibleIndex = -1
    #         addCount = 0
    #         for j in range(i+1, n):
    #             if arr[j] > arr[i] and seqCountAry[j] > addCount:
    #                 addCount = seqCountAry[j]
    #         seqCountAry[i] += addCount
    #         if maxCount < seqCountAry[i]:
    #             maxCount = seqCountAry[i]
    #     return maxCount
        
        