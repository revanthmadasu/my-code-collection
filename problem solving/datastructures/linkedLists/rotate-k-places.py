'''
    problem: https://leetcode.com/problems/rotate-list
    concepts: linked list
    performance: 37.13% runtime, 11.62% memory
    # todo: improve performance
'''
# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # iterative approach
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 0 or not head:
            return head
        numNodes = 0
        curNode = head
        lastNode = None
        while curNode != None:
            numNodes += 1
            lastNode = curNode
            curNode = curNode.next
        curNum = 0
        curNode = head
        kthNode = None
        kPrevNode = None
        while curNode != None:
            curNum += 1
            if curNum == numNodes - (k%numNodes) + 1:
                kthNode = curNode
                break
            kPrevNode = curNode
            curNode = curNode.next
        
        if numNodes == 1 or k%numNodes == 0:
            return head
        kPrevNode.next = None
        lastNode.next = head
        return kthNode
    # recursive approach - parses list only once, but has higher runtime in real time
    # def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    #     if k == 0 or not head:
    #         return head
    #     def isKthNode(curNodeNum, numNodes):
    #         l_k = k%numNodes
    #         return curNodeNum == numNodes - l_k + 1
    #     def recursiveSearch(node, numNode):
    #         if node == None:
    #             return (0, None, None, None)
    #         numNode = numNode+1
    #         if node.next:
    #             numNodes, kthNode, kPrevNode, lastNode  = recursiveSearch(node.next, numNode)
    #             if kthNode and not kPrevNode:
    #                 kPrevNode = node
    #             if not kthNode:
    #                 if isKthNode(numNode, numNodes):
    #                     kthNode = node
    #             return (numNodes, kthNode, kPrevNode, lastNode)
    #         else:
    #             return (numNode, node if isKthNode(numNode, numNode) else None, None, node)
    #     numNodes, kthNode, kPrevNode, lastNode  = recursiveSearch(head, 0)
    #     if numNodes == 1 or k%numNodes == 0:
    #         return head
    #     kPrevNode.next = None
    #     lastNode.next = head
    #     return kthNode
        