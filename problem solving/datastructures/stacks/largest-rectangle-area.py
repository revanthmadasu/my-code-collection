'''
    Problem: https://leetcode.com/problems/largest-rectangle-in-histogram/
    Concepts: Stack, Monotonic Stack
    performance: 20.44% runtime, 90.16% memory
'''
from typing import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [(heights[0], 0)]
        maxArea = heights[0]
        heights.append(-1)
        n = len(heights)

        for i in range(1, n):
            # print(f'{i} stack - {stack}, maxArea - {maxArea}')
            maxArea = max(heights[i], maxArea)
            if heights[i] > stack[-1][0]:
                stack.append((heights[i], i))
            else:
                insertIndex = i
                while len(stack) and stack[-1][0] >= heights[i]:
                    item = stack.pop()
                    area = item[0] * (i - item[1])
                    maxArea = max(area, maxArea)
                    insertIndex = item[1]
                stack.append((heights[i], insertIndex))
            # print(f'after {i} stack - {stack}, maxArea - {maxArea}')
        return maxArea