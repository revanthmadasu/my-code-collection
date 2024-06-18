'''
    Problem: https://leetcode.com/problems/linked-list-cycle-ii/
    Concepts: Linked List, Fast Slow Pointer, Floyd's Algorithm
    performance: 21.82% runtime, 68.37% memory
'''
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        once = True
        while fast and (slow != fast or once):
            once = False
            # print(f'block1 - slow: {slow.val}, fast: {fast.val}')
            slow = slow.next
            if not fast.next:
                return None
            fast = fast.next.next
        if not fast:
            return None
        slow = head
        while slow != fast:
            # print(f'block2 - slow: {slow.val}, fast: {fast.val}')
            slow = slow.next
            fast = fast.next
        return slow
