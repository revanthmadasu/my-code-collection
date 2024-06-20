'''
    Problem: https://leetcode.com/problems/sum-of-subarray-minimums
    Concepts: Stack, Monotonic Stack
    performance: 69.75% runtime, 48.46% memory
    #todo: revisit, solved using neetcode explanation
'''
from typing import List
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return arr[0]
        res = 0
        stack = []
        i = 0
        MOD = 1000000007
        arr = [float('-inf')] + arr + [float('-inf')]
        for i, num in enumerate(arr):
            while stack and num < stack[-1][1]:
                j, prevNum = stack.pop()
                left = j - stack[-1][0] if stack else j + 1
                right = i-j
                res = (res + prevNum * left * right) % MOD
            stack.append((i, num))
        # print(f'res : {res}')
        return res 