'''
    problem: https://leetcode.com/problems/merge-k-sorted-lists/description/
    concepts: LinkedLists, Recursion, Divide-and-conquer, sorting
    runtime: 19.37%, memory: 5.33%
    improve: runtime, memory
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    '''
        check if more than two are there
            if more than two are there split and make recursive call
                after splitting and making recursive calls you'll have 2 lists
                merge these two lists
            else if only two lists are there 
                merge two lists in sorted order
            return merged two lists
    '''
    def insertPivot(self, pivot, current):
        current.val = pivot.val
        return pivot.next
    def mergeKLists(self, lists):
        n = len(lists)
        listNode1 = None
        listNode2 = None
        print(f"recursive call with n = {n}")
        if n > 2:
            list1 = lists[:int(n/2)]
            list2 = lists[int(n/2):]
            print(f'calling with inp n = {len(list1)}')
            listNode1 = self.mergeKLists(list1)
            print(f'calling with inp n = {len(list2)}')
            listNode2 = self.mergeKLists(list2)
            print(f'len of list1: {len(list1)}')
            print(f'len of list2: {len(list2)}')
        elif n == 1:
            return lists[0]
        elif n == 2:
            print(f'{lists}')
            listNode1, listNode2 = lists
        else:
            return None
        pivot1 = listNode1
        pivot2 = listNode2
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