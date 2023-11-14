'''
    Problem: https://leetcode.com/problems/validate-binary-search-tree
    concepts: BST, tree traversal, trees, recusion
    performance: 75.59% runtime, 5.46% memory
    #todo: improve memory
'''
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        traversal = self.getInorder(root)
        for i in range(1, len(traversal)):
            if traversal[i-1] > traversal[i] or traversal[i-1] == traversal[i] :
                return False
        return True
    def getInorder(self, node):
        left_traversal = []
        right_traversal = []
        if node.left:
            left_traversal = self.getInorder(node.left)
        if node.right:
            right_traversal = self.getInorder(node.right)
        return [*left_traversal, node.val, *right_traversal]