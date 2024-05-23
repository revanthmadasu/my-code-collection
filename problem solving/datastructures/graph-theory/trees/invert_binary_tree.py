'''
    problem: https://leetcode.com/problems/invert-binary-tree
    concepts: trees, dfs
    performance: 37.43% runtime, 99.17% memory
'''
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if node:
                dfs(node.left)
                dfs(node.right)
                node.left, node.right = node.right, node.left
        dfs(root)
        return root
# class Solution:
#     def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
#         if root is None:
#             return root
#         nodes_to_visit = [root]
#         while len(nodes_to_visit):
#             new_nodes_to_visit = []
#             for node in nodes_to_visit:
#                 node.left, node.right = node.right, node.left
#                 if node.left:
#                     new_nodes_to_visit.append(node.left)
#                 if node.right:
#                     new_nodes_to_visit.append(node.right)
#             nodes_to_visit = new_nodes_to_visit
#         return root