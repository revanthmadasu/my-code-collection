'''
    Problem: https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
    concepts: DFS, recursion, tree traversal, trees
    performance: 19.10% runtime, 82.58% memory
    #todo: improve runtime - try a iterative solution
'''
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        results = self.recursivelyTraverse(root)
        return sum([int(res) for res in results])
    def recursivelyTraverse(self, node):
        if not node:
            return []
        all_results = []
        left_res = []
        right_res = []
        cur_node = f'{node.val}'
        if node.left:
            left_res = self.recursivelyTraverse(node.left)
        if node.right:
            right_res = self.recursivelyTraverse(node.right)
        all_results.extend(left_res)
        all_results.extend(right_res)
        if not len(all_results):
            return [cur_node]
        else:
            return [f'{cur_node}{res}' for res in all_results]
