
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
    def insertPivot(self, pivot, current):
        current.val = pivot.val
        return pivot.next
    def mergeTwoLists(self, list1, list2):
        pivot1 = list1
        pivot2 = list2
        if not pivot1 and not pivot2:
            return None
        elif not pivot1:
            return pivot2
        elif not pivot2: 
            return pivot1
        new_list = cur_node = ListNode()
        while pivot1 or pivot2:
            if ((pivot1 and pivot2) and pivot1.val < pivot2.val) or ((not (pivot1 and pivot2)) and pivot1):
                pivot1 = self.insertPivot(pivot1, cur_node)
            elif ((pivot1 and pivot2) and pivot1.val >= pivot2.val) or ((not (pivot1 and pivot2)) and pivot2):
                pivot2 = self.insertPivot(pivot2, cur_node)
            if pivot1 or pivot2:
                cur_node.next = ListNode()
                cur_node = cur_node.next
            else:
                cur_node.next = None
                break
        return new_list
    