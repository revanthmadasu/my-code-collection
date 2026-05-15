'''
    problem: https://leetcode.com/problems/trapping-rain-water
    difficulty: hard
    concepts: arrays
    performance: 58.87% runtime, 76.34% memory
'''
class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeftHeights = []
        maxRightHeights = []
        _maxLeft, _maxRight = 0, 0
        for i in range(len(height)):
            _maxLeft = max(_maxLeft, height[i])
            maxLeftHeights.append(_maxLeft)
            _maxRight = max(_maxRight, height[len(height)-1-i])
            maxRightHeights.append(_maxRight)
        maxRightHeights = maxRightHeights[::-1]
        storedWater = 0
        for i in range(len(height)):
            storedWater += max(0, min(maxRightHeights[i], maxLeftHeights[i])-height[i])
        return storedWater