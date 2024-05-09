'''
    Problem: https://leetcode.com/problems/boundary-of-binary-tree/
    Concepts: DFS, Recursion
    performance: 57.86% runtime, 78.56% memory
'''
from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(node, isLeft, isRight):
            if isLeft and (node.left or node.right):
                res.append(node.val)
            if node.left:
                dfs(node.left, isLeft, isRight and (not node.right) and node != root)
            if node.right:
                dfs(node.right, isLeft and (not node.left) and node != root, isRight)
            if not (node.left or node.right):
                res.append(node.val)
            if isRight and (node.left or node.right) and (not isLeft):
                res.append(node.val)

        dfs(root, True, True)
        return res