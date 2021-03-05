
# https://www.hackerrank.com/challenges/tree-top-view/problem

class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break
from collections import defaultdict
"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
queue = []
def topView(root):
    viewMap = defaultdict(lambda: None)
    rootNode = {
        'node': root,
        'width': 0
    }
    traverse(rootNode,viewMap)
    resultList = list(map(lambda x: viewMap[x], sorted(viewMap)))
    result = ''
    for i in resultList:
        result+=str(i) + ' '
    print(result)
def traverse(nodeObj, viewMap):
    node = nodeObj['node']
    width = nodeObj['width']
    if not node:
        if len(queue) > 0:
            traverse(queue.pop(0), viewMap)        
        return
    info = node.info
    if not viewMap[width]:
        viewMap[width] = info
    queue.append({
        'node': node.right,
        'width': width+1
    })
    queue.append({
        'node': node.left,
        'width': width-1
    })
    if len(queue) > 0:
        traverse(queue.pop(0), viewMap)     

