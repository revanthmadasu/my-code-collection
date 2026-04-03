'''
    Problem: https://leetcode.com/problems/kth-smallest-element-in-a-bst
    concepts: BST, tree traversal, trees, recusion
    performance: 80.06% runtime, 20.60% memory
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
        def inorder(node, res):
            if len(res) >= k:
                return
            if node.left:
                inorder(node.left, res)
            res.append(node.val)
            if node.right:
                inorder(node.right, res)
        res = []
        inorder(root, res)
        return res[k-1]