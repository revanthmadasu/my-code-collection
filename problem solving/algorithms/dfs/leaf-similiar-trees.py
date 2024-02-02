'''
    problem: https://leetcode.com/problems/leaf-similar-trees
    concepts: dfs, tree
    performance: 90.14% runtime, 92.80% memory
'''
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        acc1 = []
        acc2 = []
        seq1 = tuple(self.dfs(root1, acc1))
        seq2 = tuple(self.dfs(root2, acc2))
        # print(f'seq1: {seq1}')
        # print(f'seq2: {seq2}')
        return seq1 == seq2
    def dfs(self, node, acc):
        if not node:
            return acc
        if not (node.left or node.right):
            acc.append(node.val)
        else:
            if node.left:
                self.dfs(node.left, acc)
            if node.right:
                self.dfs(node.right, acc)
        return acc
        