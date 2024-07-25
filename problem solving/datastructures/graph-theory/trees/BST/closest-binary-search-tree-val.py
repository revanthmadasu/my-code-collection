'''
    problem: https://leetcode.com/problems/closest-binary-search-tree-value/
    concepts: bst, recursion, searching
    performance: 62.77% runtime, 42.97% memory
'''
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        closestTarget = root.val
        def dfs(curNode):
            # print(f'curNode: {curNode.val}')
            node2 = None
            if curNode.val == target:
                return curNode.val
            elif curNode.val > target:
                if curNode.left:
                    node2 = dfs(curNode.left)
            else:
                if curNode.right:
                    node2 = dfs(curNode.right)
            if node2 != None:
                diff1 = abs(target - curNode.val)
                diff2 = abs(target - node2)
                if diff1 == diff2:
                    return min(curNode.val, node2)
                elif diff1 < diff2:
                    return curNode.val
                else:
                    return node2
            else:
                return curNode.val
        return dfs(root)
