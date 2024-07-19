'''
    problem: https://leetcode.com/problems/longest-turbulent-subarray/
    concepts: Array, Greedy, Kadanes
    performance: 72.30% runtime, 84.05% memory
'''
from typing import List
class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        maxLen = 1
        curLen = 1
        _type = -1
        # 0 prev increased need to be decreasing now
        # 1 prev decreased need to be increasing now
        for k in range(1, len(arr)):
            if _type == 0:
                if arr[k] < arr[k-1]:
                    _type = 1
                    curLen += 1
                else:
                    _type = -1
            elif _type == 1:
                if arr[k] > arr[k-1]:
                    _type = 0
                    curLen += 1
                else:
                    _type = -1
            if _type == -1:
                if arr[k] > arr[k-1]:
                    _type = 0
                    curLen = 2
                elif arr[k] < arr[k-1]:
                    _type = 1
                    curLen = 2
                else:
                    curLen = 1
            maxLen = max(maxLen, curLen)
        return maxLen
            