'''
    Problem: https://leetcode.com/problems/subtree-of-another-tree/
    Concepts: Trees, Recursion, DFS
    performance: 40.60% runtime, 13.11% memory
'''
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def inorderTraversal(node: Optional[TreeNode], res):

            if not node:
                return res
            if node.left:
                inorderTraversal(node.left, res)
            res.append(node.val)
            if node.right:
                inorderTraversal(node.right, res)
            return res
        subRootTraversal = tuple(inorderTraversal(subRoot, []))
        # print(f'subRootTraversal is {subRootTraversal}')
        def searchForNode(node, key):
            if not node:
                return False
            if node.val == key:
                traversal = inorderTraversal(node, [])
                # print(f'traversal is {traversal}')
                if tuple(traversal) == subRootTraversal:
                    return True
            return searchForNode(node.left, key) or searchForNode(node.right, key)
        return searchForNode(root, subRoot.val)

        
