
'''
    Problem: https://leetcode.com/problems/merge-two-sorted-lists/description/
    Concepts: Linked Lists
    80% Runtime, 23% Memory 
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curNode1 = list1
        curNode2 = list2
        if not curNode1:
            return curNode2
        if not curNode2:
            return curNode1
        mergedList = None
        prevNode = None
        while curNode1 and curNode2:
            selectNode = None
            if curNode1.val <= curNode2.val:
                selectNode = curNode1
                curNode1 = curNode1.next
            else:
                selectNode = curNode2
                curNode2 = curNode2.next
            if prevNode:
                prevNode.next = selectNode
            if not mergedList:
                mergedList = selectNode
            prevNode = selectNode
        if curNode1:
            prevNode.next = curNode1
        if curNode2:
            prevNode.next = curNode2
        return mergedList