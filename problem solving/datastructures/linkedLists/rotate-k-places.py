'''
    problem: https://leetcode.com/problems/rotate-list
    concepts: linked list
    performance: 19.09% runtime, 11.62% memory
    # todo: improve performance
'''
# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 0 or not head:
            return head
        def isKthNode(curNodeNum, numNodes):
            l_k = k%numNodes
            return curNodeNum == numNodes - l_k + 1
        def recursiveSearch(node, numNode):
            if node == None:
                return (0, None, None, None)
            numNode = numNode+1
            if node.next:
                numNodes, kthNode, kPrevNode, lastNode  = recursiveSearch(node.next, numNode)
                if kthNode and not kPrevNode:
                    kPrevNode = node
                if not kthNode:
                    if isKthNode(numNode, numNodes):
                        kthNode = node
                return (numNodes, kthNode, kPrevNode, lastNode)
            else:
                return (numNode, node if isKthNode(numNode, numNode) else None, None, node)
        numNodes, kthNode, kPrevNode, lastNode  = recursiveSearch(head, 0)
        if numNodes == 1 or k%numNodes == 0:
            return head
        kPrevNode.next = None
        lastNode.next = head
        return kthNode
        