'''
    problem: https://leetcode.com/problems/valid-mountain-array/
    concepts: Arrays
    performance: 75.00% runtime, 90.13% memory
'''
from typing import List
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        leftPt = 0
        rightPt = len(arr)-1
        while leftPt < len(arr)-1 and arr[leftPt+1] > arr[leftPt]:
            leftPt += 1
        while rightPt > 0 and arr[rightPt-1] > arr[rightPt]:
            rightPt -= 1
        return leftPt == rightPt and leftPt != 0 and leftPt != len(arr)-1