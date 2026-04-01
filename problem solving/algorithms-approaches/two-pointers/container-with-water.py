'''
    Problem: https://leetcode.com/problems/container-with-most-water
    Concepts: Two pointers
    performance: 6.55% runtime, 92.75% memory
'''
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_volume = 0
        left, right = 0, len(heights) - 1
        while left < right:
            volume = min(heights[left], heights[right]) * (right - left)
            # print(f'left: {left}, right: {right}, leftHeight: {heights[left]}, rightHeight: {heights[right]}, area:{volume}')
            max_volume = max(volume, max_volume)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return max_volume