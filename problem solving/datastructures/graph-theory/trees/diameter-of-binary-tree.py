'''
    Problem: https://leetcode.com/problems/diameter-of-binary-tree/
    Concepts: Trees, Recursion, DFS
    performance: 44.48% runtime, 5.57% memory
'''
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def getLongestDiameter(node, level):
            leftLevel = level
            leftDiam = 0
            if node.left:
                leftLevel, leftDiam = getLongestDiameter(node.left, level+1)
            rightLevel = level
            rightDiam = 0
            if node.right:
                rightLevel, rightDiam = getLongestDiameter(node.right, level+1)
            curDiam = (leftLevel - level) + (rightLevel - level)
            return max(leftLevel, rightLevel), max(curDiam, leftDiam, rightDiam)
        level, diam = getLongestDiameter(root, 0)
        return diam