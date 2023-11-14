'''
    Problem: https://leetcode.com/problems/minimum-absolute-difference-in-bst
    concepts: BST, tree traversal, trees, recusion
    performance: 58.86% runtime, 56.41% memory
'''
import math
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        inorder_traversal = self.getInorder(root)
        min_diff = math.inf
        for i in range(1, len(inorder_traversal)):
            diff = abs(inorder_traversal[i] - inorder_traversal[i-1])
            if diff < min_diff:
                min_diff = diff
        return min_diff
    def getInorder(self, node):
        left_traversal = []
        right_traversal = []
        if node.left:
            left_traversal = self.getInorder(node.left)
        if node.right:
            right_traversal = self.getInorder(node.right)
        return [*left_traversal, node.val, *right_traversal]