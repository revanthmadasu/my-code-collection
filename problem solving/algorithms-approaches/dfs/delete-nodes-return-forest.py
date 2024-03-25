'''
    problem: https://leetcode.com/problems/delete-nodes-and-return-forest/
    concepts: DFS, Recursion, Tree, Binary Tree
    performance: 43.29 runtime, 89.05 memory
'''
from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        def dfs(node):
            if node is None:
                return None
            left = dfs(node.left)
            right = dfs(node.right)
            if node.val in to_delete:
                node.left = None
                node.right = None
                res.extend([left, right])
                return None
            node.left = left
            node.right = right
            return node
        res = []
        res.append(dfs(root))
        return [tree for tree in res if tree]
        