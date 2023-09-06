'''
    problem: https://leetcode.com/problems/trapping-rain-water
    difficulty: hard
    concepts: arrays
    performance: 8.27% runtime, 76.34% memory
'''
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        left_prev_highest = []
        cur_height = height[0]
        max_height = cur_height
        for i in range(n):
            cur_height = height[i]
            if cur_height > max_height:
                max_height = cur_height
            left_prev_highest.append(max_height)
        right_next_highest = []
        cur_height = height[n-1]
        max_height = cur_height
        right_next_highest = [0]*n
        for i in range(n-1, -1, -1):
            _i = n-1 - (i)
            cur_height = height[i]
            if cur_height > max_height:
                max_height = cur_height
            right_next_highest[i] = max_height
        water_stored = 0
        print('from left:')
        print(left_prev_highest)
        print('from right:')
        print(right_next_highest)
        for i in range(n):
            water_stored += min(left_prev_highest[i], right_next_highest[i]) - height[i]
        return water_stored