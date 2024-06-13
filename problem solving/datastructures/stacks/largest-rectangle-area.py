'''
    Problem: https://leetcode.com/problems/largest-rectangle-in-histogram/
    Concepts: Stack, Monotonic Stack
    #incomplete: 96/99 test cases passed
'''
from typing import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [(heights[0], 0)]
        maxArea = heights[0]
        n = len(heights)
        for i in range(1, n):
            # print(f'{i} stack - {stack}, maxArea - {maxArea}')
            maxArea = max(heights[i], maxArea)
            for stackItem in stack:
                area = min(stackItem[0], heights[i]) * (i - stackItem[1] + 1)
                maxArea = max(area, maxArea)
            if heights[i] > stack[-1][0]:
                stack.append((heights[i], i))
            elif heights[i] == 0:
                stack = [(0, i)]
            else:
                insertIndex = i
                while len(stack) and stack[-1][0] >= heights[i]:
                    item = stack.pop()
                    insertIndex = item[1]
                stack.append((heights[i], insertIndex))
            # print(f'after {i} stack - {stack}, maxArea - {maxArea}')
        return maxArea