'''
    Problem: https://leetcode.com/problems/binary-tree-inorder-traversal/
    Concepts: Trees, Recursion, DFS
    performance: 21.03% runtime, 59.80% memory
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
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.res = getattr(self, 'res', [])
        if not root:
            return self.res
        if root.left:
            self.inorderTraversal(root.left)
        self.res.append(root.val)
        if root.right:
            self.inorderTraversal(root.right)
        return self.res
        