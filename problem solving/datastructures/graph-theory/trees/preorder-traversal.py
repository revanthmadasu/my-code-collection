'''
    Problem: https://leetcode.com/problems/binary-tree-preorder-traversal/
    Concepts: Trees, Recursion, DFS
    performance: 86.83% runtime, 16.41% memory
'''
from typing import Optional
from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.res = getattr(self, 'res', [])
        if not root:
            return self.res
        self.res.append(root.val)
        if root.left:
            self.preorderTraversal(root.left)
        if root.right:
            self.preorderTraversal(root.right)
        return self.res
        