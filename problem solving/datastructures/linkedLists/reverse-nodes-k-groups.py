'''
    problem: https://leetcode.com/problems/reverse-nodes-in-k-group/
    concepts: linked list
    performance: 80.25% runtime, 31.15% memory
    #todo: improve performance
'''
from typing import Optional, ListNode
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        newHead = None
        chainPrev = None
        stack = []
        curNode = head
        if not (curNode and curNode.next):
            return head
        while curNode and curNode.next :
            # chainStart is first node in reversed chain
            chainStart = None
            chainEnd = curNode
            while len(stack) < k and curNode:
                stack.append(curNode)
                chainStart = curNode
                curNode = curNode.next
            # reverse scenario
            if len(stack) == k:
                chainEndAttach = curNode
                chainStartAttach = chainPrev

                revNode = None
                while len(stack) != 0:
                    revNode = stack.pop()
                    if len(stack):
                        revNode.next = stack[len(stack)-1]
                # now revNode is last node in reversed chain, first node in original chain
                chainEnd.next = chainEndAttach
                if chainPrev:
                    chainPrev.next = chainStart
                else:
                    newHead = chainStart
                chainPrev = chainEnd
            # curNode = chainEnd
        return newHead
