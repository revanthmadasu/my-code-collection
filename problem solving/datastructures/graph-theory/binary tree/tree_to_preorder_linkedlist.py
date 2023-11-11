'''
    Problem: https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
    concepts: DFS, recursion, tree traversal, trees
    performance: 82.99% runtime, 91.45% memory
'''
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return root
        preorder_list = []
        self.preorder(root, preorder_list)
        n = len(preorder_list)
        for i in range(n-1):
            preorder_list[i].right = preorder_list[i+1]
            preorder_list[i].left = None
        preorder_list[-1].left = None
        return root
    def preorder(self, node, order):
        order.append(node)
        if node.left:
            self.preorder(node.left, order,)
        if node.right:
            self.preorder(node.right, order)