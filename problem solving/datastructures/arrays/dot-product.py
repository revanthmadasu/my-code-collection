'''
    Problem: https://leetcode.com/problems/dot-product-of-two-sparse-vectors
    Concepts: Arrays
    performance: 59.75% runtime, 42.81% memory
'''
from typing import List
class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = nums

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        i = 0
        prod = 0
        while i< len(self.nums):
            prod += (self.nums[i] * vec.nums[i])
            i += 1
        return prod

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)