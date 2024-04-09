'''
    Problem: https://leetcode.com/problems/print-immutable-linked-list-in-reverse
    Concepts: Linked list, stack
    performance: 47.58% runtime, 15.47% memory
'''
# """
# This is the ImmutableListNode's API interface.
# You should not implement it, or speculate about its implementation.
# """
# class ImmutableListNode:
#     def printValue(self) -> None: # print the value of this node.
#     def getNext(self) -> 'ImmutableListNode': # return the next node.

class Solution:
    def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
        stack = []
        curNode = head
        while curNode:
            stack.append(curNode)
            curNode = curNode.getNext()
        while stack:
            stack.pop().printValue()