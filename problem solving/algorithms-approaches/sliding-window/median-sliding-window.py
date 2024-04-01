'''
    Problem: https://leetcode.com/problems/sliding-window-median/
    Concepts: Sliding Window
    performance: 5.02% runtime, 93.31% memory
    #todo: improve runtime -- implement insert sort
'''
import math
from typing import List
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        window = nums[:k]
        window.sort()
        medians = [(window[math.ceil((k-1)/2)]+window[math.floor((k-1)/2)])/2]
        for i in range(1, len(nums)-k+1):
            # print(f'window is {window}')
            window.remove(nums[i-1])
            window.append(nums[i+k-1])
            window.sort()
            medians.append((window[math.ceil((k-1)/2)]+window[math.floor((k-1)/2)])/2)
        return medians

# Queue implementation - timeout
# import math
# from collections import deque
# class Solution:
#     def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
#         windowAry = nums[:k]
#         windowAry.sort()
#         medians = [(windowAry[math.ceil((k-1)/2)]+windowAry[math.floor((k-1)/2)])/2]
#         windowQ = deque(windowAry)

#         for i in range(1, len(nums)-k+1):
#             # print(f'window is {window}')
#             stack = []
#             removed = False
#             while windowQ and windowQ[0] < nums[i+k-1]:
#                 popped = windowQ.popleft()
#                 if popped == nums[i-1]:
#                     if not removed:
#                         removed = True
#                         continue
#                 stack.append(popped)
#             windowQ.appendleft(nums[i+k-1])
#             if not removed:
#                 while windowQ:
#                     popped = windowQ.popleft()
#                     if popped == nums[i-1]:
#                         break
#                     stack.append(popped)
#             while stack:
#                 windowQ.appendleft(stack.pop())
#             # print(windowQ)
#             medians.append((windowQ[math.ceil((k-1)/2)]+windowQ[math.floor((k-1)/2)])/2)
            
#             # window.remove(nums[i-1])
#             # window.append(nums[i+k-1])
#             # window.sort()
#             # medians.append((window[math.ceil((k-1)/2)]+window[math.floor((k-1)/2)])/2)
#         return medians
