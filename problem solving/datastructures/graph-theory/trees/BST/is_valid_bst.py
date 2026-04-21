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

    # dfs approach    
    # def isValidBST(self, root: Optional[TreeNode]) -> bool:
    #     # returns (bool, min, max)
    #     def dfs(node):
    #         if node is None:
    #             return (True, 0, 0)
    #         leftRes = None
    #         if node.left:
    #             leftRes = dfs(node.left)
    #             if (not leftRes[0]) or leftRes[2] >= node.val:
    #                 # print(f'false at {node.}')
    #                 return (False, 0, 0)
    #         rightRes = None
    #         if node.right:
    #             rightRes = dfs(node.right)
    #             if (not rightRes[0]) or rightRes[1] <= node.val:
    #                 return (False, 0, 0)
    #         return (True, leftRes[1] if leftRes else node.val, rightRes[2] if rightRes else node.val)
    #     return dfs(root)[0]