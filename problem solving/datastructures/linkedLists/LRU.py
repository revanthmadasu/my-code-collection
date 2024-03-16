'''
    problem: https://leetcode.com/problems/lru-cache
    concepts: linked list, hashtable
    performance: 64.42% runtime, 48.73% memory
'''
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.root = None
        self.last = None
        self.currentOccupancy = 0
        self.nodesMap = dict()

    def get(self, key: int) -> int:
        # print(f'getting {key}')
        curNode = self.getKeyNode(key)
        if curNode:
            self.makeRoot(curNode)
            return curNode.val
        return -1

    def put(self, key: int, value: int) -> None:
        # print(f'putting {key} - {value}')
        curNode = self.getKeyNode(key)
        newNode = False
        if curNode:
            curNode.val = value
        else:
            newNode = True
            curNode = Node(key, value)
            self.nodesMap[key] = curNode
        self.makeRoot(curNode)
        if newNode:
            self.checkLastNode()
    def makeRoot(self, curNode):
        if curNode == self.root:
            return
        # node already in l-list
        if curNode.prev:
            if curNode == self.last:
                self.last = curNode.prev
            curNode.prev.next = curNode.next
            if curNode.next:
                curNode.next.prev = curNode.prev
        curNode.next = self.root
        if self.root:
            self.root.prev = curNode
        curNode.prev = None
        self.root = curNode
    def checkLastNode(self):
        if not self.last:
            self.last = self.root
        if not self.currentOccupancy < self.capacity:
            if self.last:
                # print(f'removing node {self.last.key}, new last node: {self.last.prev.key}')
                del self.nodesMap[self.last.key]
                self.last = self.last.prev
                self.last.next = None
        else:
            self.currentOccupancy += 1
    def getKeyNode(self, key):
        if key in self.nodesMap:
            return self.nodesMap[key]
        # curNode = self.root
        # # print(f'searching for {key}')
        # while curNode != None and curNode.key != key:
        #     # print(f'{curNode.key} -> ', end='')
        #     curNode = curNode.next
        # print('')
        # if curNode:
            # print(f'found {key}')
        return None


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)