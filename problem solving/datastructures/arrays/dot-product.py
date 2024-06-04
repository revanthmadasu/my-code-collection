'''
    Problem: https://leetcode.com/problems/dot-product-of-two-sparse-vectors
    Concepts: Arrays
    performance: 30.93% runtime, 74.40% memory
'''
from typing import List
class SparseVector:
    def __init__(self, nums: List[int]):
        self.numsDict = dict()
        for i in range(len(nums)):
            if nums[i] != 0:
                self.numsDict[i] = nums[i]

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        _sum = 0
        for i in self.numsDict:
            if i in vec.numsDict:
                _sum += (self.numsDict[i] * vec.numsDict[i])
        return _sum

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)