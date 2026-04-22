'''
    problem: https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/
    concepts: monotonous queue, sliding window, array
    performance: 21.97% runtime, 19.95% memory
'''
from collections import deque
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        minStack = deque()
        maxStack = deque()
        left = 0
        right = 0
        minStack.append((0, nums[0]))
        maxStack.append((0, nums[0]))
        maxWindowSize = 1
        def isValid():
            return maxStack[0][1] - minStack[0][1]  <= limit
        while left <= right and right < len(nums):
            # keep on increasing right expanding the window to right and break when condition breaks
            while isValid() and right+1 < len(nums):
                right += 1
                while len(minStack) and minStack[-1][1] >= nums[right]:
                    x = minStack.pop()
                while len(maxStack) and maxStack[-1][1] <= nums[right]:
                    maxStack.pop()
                minStack.append((right, nums[right]))
                maxStack.append((right, nums[right]))
                if isValid():
                    maxWindowSize = max(right - left + 1, maxWindowSize)

            # when condition breaks keep on shortening window from left
            if minStack[0][0] == left:
                minStack.popleft()
            if maxStack[0][0] == left:
                maxStack.popleft()
            left += 1
        return maxWindowSize
