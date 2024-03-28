'''
    problem: https://leetcode.com/problems/sliding-window-maximum/
    concepts: Sliding Window, Deque, Monotonic queue
    #chatgpt generated
    performance: 83.86% runtime, 86.10% memory 
'''
from typing import List
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxItems = []
        window = deque()
        for i in range(k):
            while window and nums[i] >= nums[window[-1]]:
                window.pop()
            window.append(i)
        print(f'initial window: {window}')
        for i in range(k, len(nums)):
            maxItems.append(nums[window[0]])
            '''
                [1,3,-1,-3,5,3,6,7]
                 0 1. 2  3 4 5 6 7
            '''
            while window and window[0] <= i-k:
                window.popleft()
            while window and nums[i] >= nums[window[-1]]:
                window.pop()
            window.append(i)
            print(f'{i}th window: {window}')
        maxItems.append(nums[window[0]])

        return maxItems


# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         if k == 1:
#             return nums
#         slidingWindow = nums[:k]
#         slidingWindow.sort()
#         maxItems = [slidingWindow[k-1]]
#         for i in range(1, len(nums)-k+1):
#             # print(f'bf: {slidingWindow}')
#             slidingWindow.remove(nums[i-1])
#             kthNum = nums[i+k-1]
#             if kthNum >= slidingWindow[len(slidingWindow)-1]:
#                 slidingWindow.append(kthNum)
#                 # print('appended num')
#             else:
#                 for slidingIndex in range(k-1):
#                     if kthNum < slidingWindow[slidingIndex]:
#                         slidingWindow.insert(slidingIndex, kthNum)
#                         # print('inserted num')
#                         break
#             maxItems.append(slidingWindow[len(slidingWindow)-1])
#             # print(f'af: {slidingWindow}')

#         return maxItems
    
# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         if k == 1:
#             return nums
#         slidingWindow = nums[:k]
#         slidingWindow.sort()
#         maxItems = [slidingWindow[k-1]]
#         for i in range(1, len(nums)-k+1):
#             print(f'bf: {slidingWindow}')
#             slidingWindow.remove(nums[i-1])
#             kthNum = nums[i+k-1]
#             if kthNum >= slidingWindow[len(slidingWindow)-1]:
#                 slidingWindow.append(kthNum)
#                 # print('appended num')
#             else:
#                 start = 0
#                 end = len(slidingWindow)-1
#                 insertIndex = -1
#                 while end - start > 1:
#                     mid = (start+end) // 2
#                     if slidingWindow[mid] == kthNum:
#                         insertIndex = mid
#                         break
#                     elif slidingWindow[mid] > kthNum:
#                         end = mid
#                     else:
#                         start = mid
#                     if start == end:
#                         if slidingWindow[start] >= kthNum:
#                             slidingWindow.insert(start, kthNum)
#                         else:
#                             slidingWindow.insert(start+1, kthNum)
#                     else:
#                         if kthNum <= slidingWindow[start]:
#                             slidingWindow.insert(start, kthNum)
#                         elif kthNum > slidingWindow[start] and kthNum <= slidingWindow[end]:
#                             slidingWindow.insert(end, kthNum)
#                         else:
#                             slidingWindow.insert(end+1, kthNum)
#                 # for slidingIndex in range(k-1):
#                 #     if kthNum < slidingWindow[slidingIndex]:
#                 #         slidingWindow.insert(slidingIndex, kthNum)
#                 #         # print('inserted num')
#                 #         break
#             maxItems.append(slidingWindow[len(slidingWindow)-1])
#             print(f'af: {slidingWindow}')

#         return maxItems