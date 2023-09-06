'''
    problem: https://leetcode.com/problems/trapping-rain-water
    difficulty: hard
    concepts: arrays
    performance: 58.87% runtime, 76.34% memory
'''
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        left_prev_highest = []
        cur_height_left = height[0]
        max_height_left = cur_height_left

        cur_height_right = height[n-1]
        max_height_right = cur_height_right
        right_next_highest = [0]*n
        for i in range(n):
            i_r = n-1-i
            cur_height_left = height[i]
            if cur_height_left > max_height_left:
                max_height_left = cur_height_left
            left_prev_highest.append(max_height_left)

            cur_height_right = height[i_r]
            if cur_height_right > max_height_right:
                max_height_right = cur_height_right
            right_next_highest[i_r] = max_height_right

        water_stored = 0

        for i in range(n):
            water_stored += min(left_prev_highest[i], right_next_highest[i]) - height[i]
        return water_stored