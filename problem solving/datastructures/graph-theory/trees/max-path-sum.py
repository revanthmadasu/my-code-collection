'''
    problem: https://leetcode.com/problems/binary-tree-maximum-path-sum
    concepts: tree
    performance: 88.18% runtime, 55.91% memory
'''
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self._max = float('-inf')
        def dfs(node):
            leftSum = 0
            rightSum = 0
            if node.left:
                leftSum = dfs(node.left)
            if node.right:
                rightSum = dfs(node.right)
            max_sum = max(node.val, node.val+leftSum, node.val+rightSum, node.val+leftSum+rightSum)
            max_path = max(rightSum + node.val, leftSum + node.val, node.val)
            if self._max < max_sum:
                self._max = max_sum
            return max_path


        dfs(root)
        return self._max