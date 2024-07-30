'''
    Problem: https://leetcode.com/problems/maximal-rectangle
    Concepts: Stack, Monotonic Stack, Dynamic Programming
    performance: 22.04% runtime, 55.88% memory
'''
from typing import List
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def largestRectangleArea(heights1: List[int]) -> int:
            heights = heights1.copy()
            heights.append(-1)
            maxArea = heights[0]
            stack = [(heights[0], 0)]
            for i in range(1, len(heights)):
                maxArea = max(maxArea, heights[i])
                if heights[i] > stack[-1][0]:
                    stack.append((heights[i], i))
                else:
                    insertIndex = i
                    while stack and stack[-1][0] > heights[i]:
                        h, j = stack.pop()
                        area = h * (i - j)
                        maxArea = max(area, maxArea)
                        insertIndex = j
                    stack.append((heights[i], insertIndex))
            return maxArea
        prev = [int(numStr) for numStr in matrix[0]]
        print(f'{prev}')
        maxArea = largestRectangleArea(prev)
        for i in range(1, len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "0":
                    prev[j] = 0
                else:
                    prev[j] += 1
            # print(f'calculating for {prev}')
            area = largestRectangleArea(prev)
            # print(f'area is {area}')
            maxArea = max(maxArea, largestRectangleArea(prev))
        return maxArea
