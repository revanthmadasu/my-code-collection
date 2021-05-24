#!/bin/python3

#https://www.hackerrank.com/challenges/swap-nodes-algo/problem

import math
import os
import random
import re
import sys
from collections import defaultdict

#
# Complete the 'swapNodes' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY indexes
#  2. INTEGER_ARRAY queries
#

class Node:
    depthsDict = defaultdict(lambda: None)
    deepestLevel = 1
    @staticmethod
    def __inorderTraversal(node, result):
        # print(f' Current Node {node.value}')
        if node.left:
            Node.__inorderTraversal(node.left, result)
        # print(node.value)
        result.append(node.value)
        if node.right:
            Node.__inorderTraversal(node.right, result)
        return result

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.depth = 1
        if value == 1:
            Node.depthsDict[1] = [self]
    def getInorder(self):
        return Node.__inorderTraversal(self, [])
    def addChild(self, child, direction):
        if direction == 'left':
            self.left = child
            child.parent = self
        elif direction == 'right':
            self.right = child
            child.parent = self
        child.depth = self.depth + 1
        if child.depth > Node.deepestLevel:
            Node.deepestLevel = child.depth
        if Node.depthsDict[child.depth] == None:
            Node.depthsDict[child.depth] = [child]
        else:
            Node.depthsDict[child.depth].append(child)
    def swapChildren(self):
        self.left, self.right = self.right, self.left
    def isRoot(self):
        return self.parent == None
    def isChild(self):
        return self.right == None and self.left == None
    
def swapNodes(indexes, queries):
    n = len(indexes)
    nodes = []
    result = []
    print(indexes)
    print(queries)
    for val in range(1, n+1):
        nodes.append(Node(val))
    # print(f'nodes length is {len(nodes)}')
    for i in range(n):
        currentNode = nodes[i]
        left = indexes[i][0]
        right = indexes[i][1]
        # print(f'right = {right}, left = {left}')
        if left != -1:
            leftNode = nodes[left-1]
            currentNode.addChild(leftNode, 'left')
        if right != -1:
            rightNode = nodes[right-1]
            currentNode.addChild(rightNode, 'right')
    # print('Starting Inorder traversal')
    # print(f'result is {nodes[0].getInorder()}')
    for q in queries:
        k = q
        i = 1
        while k < Node.deepestLevel:
            print(f'k is {k}')
            for node in Node.depthsDict[k]:
                node.swapChildren()
            i = i + 1
            k = i*q
        # print(f'Inorder traversal after {q} query')
        # print(f'result is {nodes[0].getInorder()}')
        result.append(nodes[0].getInorder())
    return result
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = swapNodes(indexes, queries)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()
