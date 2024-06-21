'''
    Problem: https://leetcode.com/problems/delete-node-in-a-bst/
    Concepts: BST, Trees, Recursion
    performance: 69.16% runtime, 84.24% memory
'''
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val == key:
            if root.right:
                newRoot = root.right
                curNode = newRoot
                if root.left:
                    while curNode.left:
                        curNode = curNode.left
                    curNode.left = root.left
                return newRoot
            else:
                return root.left
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            root.left = self.deleteNode(root.left, key)
        return root