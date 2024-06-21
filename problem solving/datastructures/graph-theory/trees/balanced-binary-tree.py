'''
    Problem: https://leetcode.com/problems/balanced-binary-tree/
    Concepts: Trees, Recursion, DFS
    performance: 91.22% runtime, 12.41% memory
'''
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def getLevel(node, level):
            if not node:
                return level, True
            leftLevel = level
            leftBalanced = True
            if node.left:
                leftLevel, leftBalanced = getLevel(node.left, level+1)
            if not leftBalanced:
                return -1, False
            rightLevel = level
            rightBalanced = True
            if node.right:
                rightLevel, rightBalanced = getLevel(node.right, level+1)
            if not rightBalanced:
                return -1, False
            curBalanced = abs(leftLevel-rightLevel) <= 1
            return max(leftLevel, rightLevel), curBalanced
        level, balanced = getLevel(root, 0)
        return balanced