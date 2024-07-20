'''
    problem: https://leetcode.com/problems/two-sum-bsts
    concepts: Tree, Hashtable, Recursion
    performance: 63.09% runtime, 50.62% memory
'''
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        def inOrderTraversal(curNode, countDict):
            if not curNode:
                return
            inOrderTraversal(curNode.left, countDict)
            countDict[curNode.val] = True
            inOrderTraversal(curNode.right, countDict)
        countDict1 = dict()
        countDict2 = dict()
        inOrderTraversal(root1, countDict1)
        inOrderTraversal(root2, countDict2)
        for key1 in countDict1:
            req = target - key1
            if req in countDict2:
                return True
        return False
        
        