'''
    Problem: https://leetcode.com/problems/insert-into-a-binary-search-tree/
    Concepts: BST, Trees, Recursion
    performance: 17.21% runtime, 87.53% memory
'''
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val=val)
        if val < root.val:
            if root.left:
                self.insertIntoBST(root.left, val)
            else:
                node = TreeNode(val=val)
                root.left = node
        else:
            if root.right:
                self.insertIntoBST(root.right, val)
            else:
                node = TreeNode(val=val)
                root.right = node
        return root