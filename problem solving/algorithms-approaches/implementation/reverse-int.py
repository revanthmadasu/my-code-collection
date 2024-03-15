'''
    problem: https://leetcode.com/problems/reverse-integer
    concepts: strings, numbers
    runtime: 75.3%, memory: 18.35%
'''
class Solution:
    def reverse(self, x: int) -> int:
        range_min = -2147483648
        range_max = 2147483647
        nums = str(x).split('-')
        if len(nums) > 1:
            reversed_num = int(nums[1][::-1])
            reversed_num *= -1
        else:
            reversed_num = int(nums[0][::-1])
        if reversed_num < range_min or reversed_num > range_max:
            return 0
        return reversed_num