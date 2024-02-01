'''
    problem: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
    concepts: bst, recursion, divide and conquer
    performance: 72.64% runtime, 58.60% memory
'''
from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.recursiveCreateNodes(nums)
    def recursiveCreateNodes(self, nums):
        # print(f'nums: {nums}')
        mid = int(len(nums)/2)
        left_nums = nums[:mid]
        right_nums = nums[(mid+1):]
        node = TreeNode(nums[mid])
        if len(right_nums):
            # print(f'attaching {right_nums} to right child of {nums[mid]}')
            right_node = self.recursiveCreateNodes(right_nums)
            node.right = right_node
        if len(left_nums):
            left_node = self.recursiveCreateNodes(left_nums)
            node.left = left_node
        return node
        