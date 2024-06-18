'''
    Problem: https://leetcode.com/problems/find-the-duplicate-number/
    Concepts: Linked List, Fast Slow Pointer, Floyd's Algorithm
    performance: 7.29% runtime, 24.71% memory
'''
from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        slow = 0
        while slow != fast:
            # print(f'slow: {slow} fast: {fast}')
            slow = nums[slow]
            fast = nums[fast]
        return slow