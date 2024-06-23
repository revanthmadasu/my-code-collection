'''
    Problem: https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/
    Concepts: Prefix Sum, Hashtable
    performance: 8.73.57% runtime, 20.32% memory
'''
from typing import List
class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        prefixSum = [0]
        _sum = 0
        occDict = dict()
        occDict[0] = 0
        for i, num in enumerate(nums):
            _sum += num
            prefixSum.append(_sum)
            occDict[_sum] = i+1
        i = 0
        # print(f'prefix sum : {prefixSum}')
        maxLen = 0
        for i in range(0, len(prefixSum)):
            if (k+prefixSum[i]) in occDict:
                j = occDict[k+prefixSum[i]]
                # print(f'i is {i}, j is {j}')
                maxLen = max(maxLen, j-i)
            if occDict[prefixSum[i]] == i:
                del occDict[prefixSum[i]]
        # brute force
        # while i < len(prefixSum):
        #     j = i+1
        #     while j < len(prefixSum):
        #         if prefixSum[j] - prefixSum[i] == k:
        #             maxLen = max(maxLen, j-i)
        #         j += 1
        #     i += 1
        return maxLen