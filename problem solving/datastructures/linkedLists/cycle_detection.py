'''
    problem: https://leetcode.com/problems/linked-list-cycle/
    concepts: recursion, linked lists
    performance: 24.75% runtime, 5.85% memory
    #todo - improve runtime, memory
'''
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

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