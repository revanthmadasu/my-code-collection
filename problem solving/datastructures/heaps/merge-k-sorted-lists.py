'''
    problem: https://leetcode.com/problems/merge-k-sorted-lists/
    Concepts: Linked lists, two pointers
    performance: 21% runtime, 26% memory
'''
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Heap:
    def __init__(self, key_fn = None):
        self.vals = []
        self.key_fn = key_fn
    def peek(self):
        if len(self.vals):
            return self.vals[0]
        return None
    def getVal(self, index):
        if self.key_fn:
            return self.key_fn(self.vals[index])
        else:
            return self.vals[index]

    def getChildrenIndices(self, nodeIndex):
        return {'left': nodeIndex*2 +1, 'right': nodeIndex*2 + 2}

    def getParentIndex(self, childIndex):
        return max(int((childIndex-1)/2), 0)
    
    def heapifyDown(self):
        cur = 0

        def isConsistent(nodeIndex):
            childs = self.getChildrenIndices(cur)
            minNodeI = nodeIndex
            consistent = True
            if childs['left'] < len(self.vals):
                if self.getVal(childs['left']) < self.getVal(minNodeI):
                    minNodeI = childs['left']
                    consistent = False
            if childs['right'] < len(self.vals):
                if self.getVal(childs['right']) < self.getVal(nodeIndex):
                    if self.getVal(childs['right']) < self.getVal(minNodeI):
                        minNodeI = childs['right']
                    consistent = False
            return [consistent, minNodeI]

        [consistent, minNodeI] = isConsistent(cur)
        while not consistent:
            self.vals[minNodeI], self.vals[cur] = self.vals[cur], self.vals[minNodeI]
            cur = minNodeI
            [consistent, minNodeI] = isConsistent(cur)
    def heapifyUp(self):
        cur = len(self.vals)-1
        parent = self.getParentIndex(cur)
        while self.getVal(parent) > self.getVal(cur):
            self.vals[parent], self.vals[cur] = self.vals[cur], self.vals[parent]
            cur = parent
            parent = self.getParentIndex(cur)
    def push(self, val):
        self.vals.append(val)
        self.heapifyUp()
    def pop(self):
        val = self.vals[0]
        self.vals[0] = self.vals[len(self.vals) - 1]
        self.vals.pop(len(self.vals) - 1)
        self.heapifyDown()
        return val
    def isEmpty(self):
        return len(self.vals) == 0

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        my_heap = Heap(lambda node: node['val'] if node else None)
        for llist in lists:
            if llist:
                my_heap.push(llist)
        root = None
        cur_node = None
        while not my_heap.isEmpty():
            least_node = my_heap.pop()
            new_node = ListNode(least_node['val'])
            if cur_node is None:
                root = cur_node = new_node
            else:
                cur_node.next = new_node
                cur_node = cur_node.next
            updated_node = least_node['next']
            if updated_node:
                my_heap.push(updated_node)
        return root
def printLList(l):
    c = l
    while c:
        print(f'-> {c.val}', end=' ')
        c = c.next
sol = Solution()
test_lists1 = [
    {
        'val': 1,
        'next': {
            'val': 4,
            'next': {
                'val': 5,
                'next': None
            }
        }
    },
    {
        'val': 1,
        'next': {
            'val': 3,
            'next': {
                'val': 4,
                'next': None
            }
        }
    },
    {
        'val': 2,
        'next': {
            'val': 6,
            'next': None
        }
    }
]

printLList(sol.mergeKLists(test_lists1))


'''
    submission sol:

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Heap:
    def __init__(self, key_fn = None):
        self.vals = []
        self.key_fn = key_fn
    def peek(self):
        if len(self.vals):
            return self.vals[0]
        return None
    def getVal(self, index):
        if self.key_fn:
            return self.key_fn(self.vals[index])
        else:
            return self.vals[index]

    def getChildrenIndices(self, nodeIndex):
        return {'left': nodeIndex*2 +1, 'right': nodeIndex*2 + 2}

    def getParentIndex(self, childIndex):
        return max(int((childIndex-1)/2), 0)
    
    def heapifyDown(self):
        cur = 0

        def isConsistent(nodeIndex):
            childs = self.getChildrenIndices(cur)
            minNodeI = nodeIndex
            consistent = True
            if childs['left'] < len(self.vals):
                if self.getVal(childs['left']) < self.getVal(minNodeI):
                    minNodeI = childs['left']
                    consistent = False
            if childs['right'] < len(self.vals):
                if self.getVal(childs['right']) < self.getVal(nodeIndex):
                    if self.getVal(childs['right']) < self.getVal(minNodeI):
                        minNodeI = childs['right']
                    consistent = False
            return [consistent, minNodeI]

        [consistent, minNodeI] = isConsistent(cur)
        while not consistent:
            self.vals[minNodeI], self.vals[cur] = self.vals[cur], self.vals[minNodeI]
            cur = minNodeI
            [consistent, minNodeI] = isConsistent(cur)
    def heapifyUp(self):
        cur = len(self.vals)-1
        parent = self.getParentIndex(cur)
        while self.getVal(parent) > self.getVal(cur):
            self.vals[parent], self.vals[cur] = self.vals[cur], self.vals[parent]
            cur = parent
            parent = self.getParentIndex(cur)
    def push(self, val):
        self.vals.append(val)
        self.heapifyUp()
    def pop(self):
        val = self.vals[0]
        self.vals[0] = self.vals[len(self.vals) - 1]
        self.vals.pop(len(self.vals) - 1)
        self.heapifyDown()
        return val
    def isEmpty(self):
        return len(self.vals) == 0

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        my_heap = Heap(lambda node: node.val if node else None)
        for llist in lists:
            if llist:
                my_heap.push(llist)
        root = None
        cur_node = None
        while not my_heap.isEmpty():
            least_node = my_heap.pop()
            if least_node is None:
                break
            # print('creating node: ',least_node.val)
            new_node = ListNode(least_node.val)
            if cur_node is None:
                root = cur_node = new_node
            else:
                cur_node.next = new_node
                cur_node = cur_node.next
            updated_node = least_node.next
            if updated_node:
                my_heap.push(updated_node)
        return root
        
'''