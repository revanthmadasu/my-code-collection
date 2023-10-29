'''
    problem: https://leetcode.com/problems/linked-list-cycle/
    concepts: recursion, linked lists
    performance: 96.32% Runtime, 38.44% memory
'''
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# recursive approach
# performance: 24.75% runtime, 5.85% memory
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        if not getattr(head, "visited", False):
            if head.next != None:
                head.visited = True
                return self.hasCycle(head.next)
            else:
                return False
        else:
            return True

# loops approach     
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        while head:
            if not getattr(head, "visited", False):
                if head.next != None:
                    head.visited = True
                    head = head.next
                    continue
                else:
                    return False
            else:
                return True