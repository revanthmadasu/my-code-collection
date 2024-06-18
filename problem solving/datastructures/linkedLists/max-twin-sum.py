'''
    Problem: https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/
    Concepts: Linked List, Fast Slow Pointer, Stack
    performance: 57.33% runtime, 6.92% memory
'''
'''
1,2,3,4,5,6
fast: 1,3,5
slow: 1,2,3
'''
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head
        stack = []
        while fast:
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next
        maxSum = float('-inf')
        while slow:
            maxSum = max(stack.pop() + slow.val, maxSum)
            slow = slow.next
        return maxSum
