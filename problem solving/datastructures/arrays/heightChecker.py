'''
    Problem: https://leetcode.com/problems/height-checker
    Concepts: Arrays, sorting
    performance: 11.16% runtime, 87.40% memory
    #todo: improve runtime
'''
from typing import List
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sortedHeights = sorted(heights)
        mismatched = 0
        for i in range(len(heights)):
            mismatched += int(heights[i] != sortedHeights[i])
        return mismatched