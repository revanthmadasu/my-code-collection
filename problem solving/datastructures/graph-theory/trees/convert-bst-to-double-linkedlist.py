'''
    problem: https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/
    concepts: Tree, Linked List, Recursion
    performance: 44.94% runtime, 6.01% memory
'''
from typing import Optional
"""
# Definition for a Node.
"""
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        def convertRecursively(curNode, parNode, direction):
            if not curNode:
                return None, None
            if (not curNode.left) and (not curNode.right):
                if direction == 'left':
                    curNode.right = parNode
                    parNode.left = curNode
                elif direction == 'right':
                    curNode.left = parNode
                    parNode.right = curNode
                return (curNode, curNode)
            utMostLeft = curNode
            utMostRight = curNode
            if curNode.left:
                left, right = convertRecursively(curNode.left, curNode, 'left')
                curNode.left = right
                utMostLeft = left
            if curNode.right:
                left, right = convertRecursively(curNode.right, curNode, 'right')
                curNode.right = left
                utMostRight = right
            if direction == 'left':
                utMostRight.right = parNode
                parNode.left = utMostRight
            elif direction == 'right':
                utMostLeft.left = parNode
                parNode.right = utMostLeft

            return utMostLeft, utMostRight
        if root is None:
            return None
        utMostLeft, utMostRight = root, root
        if root.left:
            left, right1 = convertRecursively(root.left, root, 'left')
            utMostLeft = left
        if root.right:
            left1, right = convertRecursively(root.right, root, 'right')
            utMostRight = right
        utMostLeft.left = utMostRight
        utMostRight.right = utMostLeft
        return utMostLeft
                