'''
    Problem: https://leetcode.com/problems/random-pick-index
    Concepts: Hashtable, Random
    performance: 72.24% runtime, 13.34% memory
'''
from typing import List
import random
class Solution:

    def __init__(self, nums: List[int]):
        self.indices = dict()
        for i in range(len(nums)):
            num = nums[i]
            if num not in self.indices:
                self.indices[num] = []
            self.indices[num].append(i)

    def pick(self, target: int) -> int:
        return self.indices[target][int(random.random() * len(self.indices[target]))]


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)