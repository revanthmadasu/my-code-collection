'''
    problem: https://leetcode.com/problems/symmetric-tree
    concepts: trees, dfs
    performance: 72.96% runtime, 52.85% memory
'''
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.determineSumRecursively(root, 0, targetSum) if root is not None else False
    def determineSumRecursively(self, node, acc_sum, target_sum):
        # print(f'node: {node.val if node else node}, acc_sum: {acc_sum}, target_sum: {target_sum}')
        if not node:
            return acc_sum == target_sum
        cur_sum = acc_sum + node.val
        if (not node.left) and (not node.right):
            return cur_sum == target_sum
        left_sum_matched = False
        right_sum_matched = False
        if node.left:
            left_sum_matched = self.determineSumRecursively(node.left, cur_sum, target_sum)
        if node.right:
            right_sum_matched = self.determineSumRecursively(node.right, cur_sum, target_sum)
        return left_sum_matched or right_sum_matched
        
        