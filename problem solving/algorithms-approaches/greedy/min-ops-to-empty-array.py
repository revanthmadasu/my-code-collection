'''
    Problem: https://leetcode.com/problems/minimum-number-of-operations-to-make-array-empty/
    Concepts: Greedy, Hashtable
    performance: 16.58% runtime, 55.06% memory
'''
from typing import List
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        numsCount = dict()
        for num in nums:
            if num not in numsCount:
                numsCount[num] = 0
            numsCount[num] += 1
        opCount = 0
        for num in numsCount:
            if numsCount[num] == 1:
                return -1
            
            twoOpCount = numsCount[num]//2 - (numsCount[num]%2)
            threeOpCount = numsCount[num]%2
            twoOpRemoval = twoOpCount // 3
            twoOpCount = twoOpCount - (twoOpRemoval*3)
            threeOpCount = threeOpCount + (twoOpRemoval*2)
            opCount += (threeOpCount + twoOpCount)
        return opCount