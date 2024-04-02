'''
    Problem: https://leetcode.com/problems/palindrome-linked-list/
    Concepts: Linked List, Stack
    performance: 14.46% runtime, 27.26% memory
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = []
        cur = head
        while cur:
            stack.append(cur.val)
            cur = cur.next
        cur = head
        while cur:
            if stack.pop() != cur.val:
                return False
            cur = cur.next
        return True