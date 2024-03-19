'''
    problem: https://leetcode.com/problems/partition-list
    concepts: linkedlist
    performance: 18.59% runtime, 69.44% memory
'''
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        lesserHead, greaterHead, curLesser, curGreater = None, None, None, None
        curNode = head
        while curNode:
            if curNode.val < x:
                if not lesserHead:
                    lesserHead = curNode
                    curLesser = curNode
                else:
                    curLesser.next = curNode
                    curLesser = curLesser.next
            else:
                if not greaterHead:
                    greaterHead = curNode
                    curGreater = curNode
                else:
                    curGreater.next = curNode
                    curGreater = curGreater.next
            curNode = curNode.next
        if curLesser and greaterHead:
            curLesser.next = greaterHead
        if curGreater:
            curGreater.next = None
        if lesserHead:
            return lesserHead
        return greaterHead

