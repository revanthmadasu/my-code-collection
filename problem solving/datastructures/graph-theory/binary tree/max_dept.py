'''
    Problem: https://leetcode.com/problems/maximum-depth-of-binary-tree
    concepts: Binary Tree, Tree Traversal, bfs
    performance: 99.80% runtime, 99.79% memory
'''
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        nodes_to_visit = [root]
        depth = 0
        while len(nodes_to_visit):
            depth += 1
            next_nodes_to_visit = []
            for visiting_node in nodes_to_visit:
                if visiting_node.left:
                    next_nodes_to_visit.append(visiting_node.left)
                if visiting_node.right:
                    next_nodes_to_visit.append(visiting_node.right)
            nodes_to_visit = next_nodes_to_visit
        return depth
            
        