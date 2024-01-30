'''
    problem: https://leetcode.com/problems/kth-largest-element-in-an-array
    concepts: heaps
    performance: 5.02% runtime, 91.54% memory
'''
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
                if self.getVal(childs['left']) > self.getVal(minNodeI):
                    minNodeI = childs['left']
                    consistent = False
            if childs['right'] < len(self.vals):
                if self.getVal(childs['right']) > self.getVal(nodeIndex):
                    if self.getVal(childs['right']) > self.getVal(minNodeI):
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
        while self.getVal(parent) < self.getVal(cur):
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
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap = Heap()
        for num in nums:
            heap.push(num)
        res = nums[0]
        for i in range(k):
            res = heap.pop()
            print('popped: ', res)
        return res
        
sol = Solution()

print(sol.findKthLargest([3,2,3,1,2,4,5,5,6], 4))