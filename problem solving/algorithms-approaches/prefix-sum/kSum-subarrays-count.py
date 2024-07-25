'''
    Problem: https://leetcode.com/problems/subarray-sum-equals-k
    Concepts: Prefix Sum, Hashtable
    performance: 5.06% runtime, 13.41% memory
'''
from typing import List
'''
1,2,3,-1,0
0,1,3,6,5,5

0:0
1:1
3:2
6:3
5:4,5
'''
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSumDict = dict()
        prefixSumDict[0] = [0]
        _sum = 0
        for i in range(len(nums)):
            _sum += nums[i]
            if _sum not in prefixSumDict:
                prefixSumDict[_sum] = []
            prefixSumDict[_sum].append(i+1)
        subarrays = 0
        for key in prefixSumDict:
            if key+k in prefixSumDict:
                for i in prefixSumDict[key]:
                    subarrays += len([j for j in prefixSumDict[key+k] if j > i])
        return subarrays
