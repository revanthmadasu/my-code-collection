'''
    problem: https://leetcode.com/problems/symmetric-tree
    concepts: trees, bfs
    performance: 64.72% runtime, 18.60% memory
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
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        p = root.left
        q = root.right
        if p is None or q is None:
            return p is None and q is None
        nodes_to_visit_p = [p]
        nodes_to_visit_q = [q]
        p_len = 1
        q_len = 1
        while p_len and q_len:
            next_nodes_to_visit_p = []
            next_nodes_to_visit_q = []
            n = len(nodes_to_visit_p)
            for i in range(n):
                p_node = nodes_to_visit_p[i]
                q_node = nodes_to_visit_q[i]
                if p_node.val != q_node.val:
                    return False
                if p_node.left or q_node.right:
                    if not (p_node.left and q_node.right):
                        return False
                    else:
                        if p_node.left.val != q_node.right.val:
                            return
                    next_nodes_to_visit_p.append(p_node.left)
                    next_nodes_to_visit_q.append(q_node.right)
                if p_node.right or q_node.left:
                    if not (p_node.right and q_node.left):
                        return False
                    else:
                        if p_node.right.val != q_node.left.val:
                            return
                    next_nodes_to_visit_p.append(p_node.right)
                    next_nodes_to_visit_q.append(q_node.left)
            nodes_to_visit_p = next_nodes_to_visit_p
            nodes_to_visit_q = next_nodes_to_visit_q
            p_len = len(nodes_to_visit_p)
            q_len = len(nodes_to_visit_q)
            if p_len != q_len:
                return False
        return True