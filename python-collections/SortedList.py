class L_Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
    def append(self, successor):
        self.next = successor
        successor.prev = self
    def changePredecessor(self, insertingNode):
        prevNode = self.prev
        if prevNode:
            prevNode.append(insertingNode)
        insertingNode.append(self)

'''
This uses linked lists. The performance can be improved if the data structure is changed to Binary or AVL trees
'''
class SortedList:
    def __init__(self, key):
        self.s_list = None
        self.key = key
        self.length = 0
    def add_item(self, item):
        print(f'Current number: {item[self.key]}')
        if self.s_list:
            cur_node = self.s_list
            while True:
                # adding item comes before current node
                addingNode = L_Node(item)
                if item[self.key] < cur_node.value[self.key]:
                    # current node is root node
                    if cur_node.prev == None:
                        addingNode.append(cur_node)
                        self.s_list = addingNode
                        print('added to first')
                        break
                    else:
                        cur_node.changePredecessor(addingNode)
                        print('added in middle')
                        break
                # if cur_node comes before
                else:
                    if cur_node.next:
                        cur_node = cur_node.next
                        print('skipping')
                    else:
                        cur_node.append(addingNode)
                        print('added at last')
                        break
        else:
            self.s_list = L_Node(item)
    def pop(self):
        cur_node = self.s_list
        while cur_node.next != None:
            cur_node = cur_node.next
        if cur_node.prev:
            cur_node.prev.next = None
            cur_node.prev = None
        return cur_node
    
    def printAll(self):
        cur_node = self.s_list
        while cur_node.next != None:
            print(f'{cur_node.value}', end=' ')
            cur_node = cur_node.next
        print(cur_node.value)

print('hi')
myList = SortedList('num')
nums = [2,5,3,5,1,6,7]
mappedNums = [{'num': num} for num in nums]
for mappedNum in mappedNums:
    myList.add_item(mappedNum)
myList.printAll()