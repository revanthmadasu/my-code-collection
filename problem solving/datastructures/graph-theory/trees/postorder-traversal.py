'''
    Problem: https://leetcode.com/problems/binary-tree-postorder-traversal/
    Concepts: Trees, Recursion, DFS
    performance: 64.37% runtime, 16.59% memory
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
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.res = getattr(self, 'res', [])
        if not root:
            return self.res
        if root.left:
            self.postorderTraversal(root.left)
        if root.right:
            self.postorderTraversal(root.right)
        self.res.append(root.val)
        return self.res