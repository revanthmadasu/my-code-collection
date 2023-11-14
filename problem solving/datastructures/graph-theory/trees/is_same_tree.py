'''
    problem: https://leetcode.com/problems/same-tree/
    concepts: trees, bfs
    performance: 56.40% runtime, 61.79% memory
'''
# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None or q is None:
            return p is None and q is None
        nodes_to_visit_p = [p]
        nodes_to_visit_q = [q]
        while len(nodes_to_visit_p) and len(nodes_to_visit_q) :
            next_nodes_to_visit_p = []
            next_nodes_to_visit_q = []
            n = len(nodes_to_visit_p)
            print(f'p_n is {n}')
            print(f'q_n is {len(nodes_to_visit_q)}')
            for i in range(n):
                print(f'i is {i}')
                p_node = nodes_to_visit_p[i]
                q_node = nodes_to_visit_q[i]
                if p_node.val != q_node.val:
                    return False
                if p_node.left or q_node.left:
                    if not (p_node.left and q_node.left):
                        return False
                    next_nodes_to_visit_p.append(p_node.left)
                    next_nodes_to_visit_q.append(q_node.left)
                if p_node.right or q_node.right:
                    if not (p_node.right and q_node.right):
                        return False
                    next_nodes_to_visit_p.append(p_node.right)
                    next_nodes_to_visit_q.append(q_node.right)
            nodes_to_visit_p = next_nodes_to_visit_p
            nodes_to_visit_q = next_nodes_to_visit_q
            if len(nodes_to_visit_p) != len(nodes_to_visit_q):
                return False
        return True
    def runTestCases(self):

        # Testcase 1
        node_2_p = TreeNode(2)
        node_2_q = TreeNode(2)
        node_3_p = TreeNode(3)
        node_3_q = TreeNode(3)
        node_1_p = TreeNode(1, node_2_p, node_3_p)
        node_1_q = TreeNode(1, node_2_q, node_3_q)
        print(self.isSameTree(node_1_p, node_1_q))

        # ========================================================

        # Testcase 2

Solution().runTestCases()