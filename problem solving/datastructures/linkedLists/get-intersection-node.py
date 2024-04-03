'''
    problem: https://leetcode.com/problems/intersection-of-two-linked-lists/
    concepts: Linked List, Two Pointers
    performance: 35.95 runtime, 5.99 memory
'''
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        nodes = set()
        p1 = headA
        p2 = headB
        while p1 or p2:
            if p1:
                if id(p1) in nodes:
                    return p1
                nodes.add(id(p1))
                p1 = p1.next
            if p2:
                if id(p2) in nodes:
                    return p2
                nodes.add(id(p2))
                p2 = p2.next
        return None