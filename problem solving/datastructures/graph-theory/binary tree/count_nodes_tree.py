'''
    problem: https://leetcode.com/problems/count-complete-tree-nodes
    concepts: trees, bfs
    performance: 64.40% runtime, 9.37% memory
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
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        nodes_to_visit = [root]
        nodes_len = 1
        nodes_count = 0
        while nodes_len:
            nodes_count += nodes_len
            next_nodes_to_visit = []
            for visiting_node in nodes_to_visit:
                if visiting_node.left:
                    next_nodes_to_visit.append(visiting_node.left)
                if visiting_node.right:
                    next_nodes_to_visit.append(visiting_node.right)
            nodes_to_visit = next_nodes_to_visit
            nodes_len = len(nodes_to_visit)
        return nodes_count