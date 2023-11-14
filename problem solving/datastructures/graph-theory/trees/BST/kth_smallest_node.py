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
        self.k = k
        inorder_traversal, l = self.getInorder(root)
        return inorder_traversal[k-1]
    def getInorder(self, node):
        left_traversal = []
        right_traversal = []
        l = 1
        ll = 0
        rl = 0
        if node.left:
            left_traversal, ll = self.getInorder(node.left)
            # if traversal reaches upto k nodes then no need to visit right subtree
            if ll + l > self.k:
                traversal = [*left_traversal, node.val]
                return (traversal, l+ll)
        if node.right:
            right_traversal, rl = self.getInorder(node.right)
        traversal = [*left_traversal, node.val, *right_traversal]
        return (traversal, l+ll+rl)