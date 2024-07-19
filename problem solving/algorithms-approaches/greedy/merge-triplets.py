'''
    problem: https://leetcode.com/problems/merge-triplets-to-form-target-triplet/
    concepts: Array, Greedy
    performance: 52.95% runtime, 81.43% memory
'''
from typing import List
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        firstMatch = False
        secondMatch = False
        thirdMatch = False
        i = 0
        while i < len(triplets) and not (firstMatch and secondMatch and thirdMatch):
            if triplets[i][0] == target[0] and triplets[i][1] <= target[1] and triplets[i][2] <= target[2]:
                firstMatch = True
            if triplets[i][1] == target[1] and triplets[i][0] <= target[0] and triplets[i][2] <= target[2]:
                secondMatch = True
            if triplets[i][2] == target[2] and triplets[i][0] <= target[0] and triplets[i][1] <= target[1]:
                thirdMatch = True
            i += 1
        return firstMatch and secondMatch and thirdMatch
