'''
    problem: https://leetcode.com/problems/binary-tree-maximum-path-sum
    concepts: tree
    performance: 58.68% runtime, 31.42% memory
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
            _sum = 0
            leftSum = 0
            rightSum = 0
            if node.left:
                leftSum = dfs(node.left)
                _sum = leftSum
            if node.right:
                rightSum = dfs(node.right)
                if rightSum > _sum:
                    _sum = rightSum
            max_sum = max(node.val, node.val+leftSum, node.val+rightSum, node.val+leftSum+rightSum)
            max_path = max(_sum + node.val, node.val)
            if self._max < max_sum:
                self._max = max_sum
            return max_path

        dfs(root)
        return self._max