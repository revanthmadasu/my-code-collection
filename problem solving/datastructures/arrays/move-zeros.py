# https://leetcode.com/problems/move-zeroes/
class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        num_zero = 0
        for i in range(n):
            if nums[i] == 0:
                num_zero += 1
            elif num_zero:
                nums[i-num_zero] = nums[i]
                nums[i] = 0
            