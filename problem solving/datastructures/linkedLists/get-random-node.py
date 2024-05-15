'''
    Problem: https://leetcode.com/problems/linked-list-random-node
    Concepts: Linked list, random
    performance: 31.37% runtime, 11.32% memory
'''
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
import random
class Solution:

    def __init__(self, head: Optional[ListNode]):
        pointer = head
        count = 0
        while pointer:
            count += 1
            pointer = pointer.next
        self.size = count
        if self.size == 0:
            if head:
                self.size = 1
        self.head = head

    def getRandom(self) -> int:

        rand = random.randint(0, self.size-1)
        i = 0
        cur = self.head
        while cur and cur.next and i != rand:
            cur = cur.next
            i += 1
        return cur.val


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()