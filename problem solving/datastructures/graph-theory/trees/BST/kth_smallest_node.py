'''
    Problem: https://leetcode.com/problems/kth-smallest-element-in-a-bst
    concepts: BST, tree traversal, trees, recusion
    performance: 39.22% runtime, 20.60% memory
    #todo: improve performance
'''
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        inorder_traversal = self.getInorder(root)
        return inorder_traversal[k-1]
    def getInorder(self, node):
        left_traversal = []
        right_traversal = []
        if node.left:
            left_traversal = self.getInorder(node.left)
        if node.right:
            right_traversal = self.getInorder(node.right)
        return [*left_traversal, node.val, *right_traversal]