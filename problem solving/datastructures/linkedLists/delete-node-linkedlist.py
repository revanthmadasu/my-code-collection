'''
    Problem: https://leetcode.com/problems/delete-node-in-a-linked-list
    Concepts: Linked List
    performance: 51.98% runtime, 35.62% memory
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        curNode = node
        while curNode.next.next:
            curNode.val = curNode.next.val
            curNode = curNode.next
        curNode.val = curNode.next.val
        curNode.next = None
        