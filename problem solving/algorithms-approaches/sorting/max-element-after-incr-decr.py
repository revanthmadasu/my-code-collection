'''
    problem: https://leetcode.com/problems/maximum-element-after-decreasing-and-rearranging/
    concepts: Array, Sorting, Greedy
    performance: 68.04% runtime, 18.39% memory
'''
from typing import List
class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        arr[0] = 1
        for i in range(1, len(arr)):
            if arr[i]-arr[i-1] > 1:
                arr[i] = arr[i-1] + 1
        return arr[-1]