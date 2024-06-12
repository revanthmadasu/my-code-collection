'''
    Problem: https://leetcode.com/problems/daily-temperatures/
    Concepts: Stack, Monotonic Stack
    performance: 69.78% runtime, 81.29% memory
'''
from collections import deque
from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = deque()
        stack.append(0)
        ans = [0] * len(temperatures)
        for i in range(1,len(temperatures)):
            while len(stack) and temperatures[i] > temperatures[stack[-1]]:
                lastItem = stack.pop()
                # print(f'{lastItem}, {i}')
                ans[lastItem] = i - lastItem
            stack.append(i)
        return ans
        # brute force approach
        # res = []
        # for i in range(len(temperatures)):
        #     found = False
        #     for j in range(i, len(temperatures)):
        #         if temperatures[j] > temperatures[i]:
        #             found = True
        #             res.append(j-i)
        #             break
        #     if not found:
        #         res.append(0)
        # return res