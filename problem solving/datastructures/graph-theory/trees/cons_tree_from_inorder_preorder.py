'''
    problem: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
    concepts: binary tree, tree traversals, divide and conquer, recursion, hash-table
    performance: 65.58% runtime, 5.18% memory
    # todo - improve memory - try if iterative solution improves memory
'''
from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        root = None
        in_index_map = dict()
        n = len(preorder)
        for i in range(n):
            in_index_map[inorder[i]] = i
        self.in_index_map = in_index_map
        return self.createTreeRecursively(preorder, inorder)
    def createTreeRecursively(self, preorder, inorder):
        head = preorder[0]
        head_node = TreeNode(head)
        curr_len = len(preorder)
        # left child is not present
        no_left_child = inorder[0] == head
        no_right_child = inorder[curr_len - 1] == head

        head_in_index = self.in_index_map[head]
        start_in_index = self.in_index_map[inorder[0]]
        cur_head_in_index = head_in_index - start_in_index
        if no_left_child and no_right_child:
            return head_node
        if not no_left_child:
            next_inorder = inorder[0:cur_head_in_index]
            next_preorder = preorder[1:cur_head_in_index+1]
            head_node.left = self.createTreeRecursively(next_preorder, next_inorder)
        if not no_right_child:
            next_inorder = inorder[cur_head_in_index+1:]
            # todo - to improve runtime use the index map to calculate length
            next_inorder_len = len(next_inorder)
            next_preorder = preorder[-next_inorder_len:]
            head_node.right = self.createTreeRecursively(next_preorder, next_inorder)
        return head_node