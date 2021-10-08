#!/bin/python3
#https://www.hackerrank.com/challenges/even-tree/problem
import math
import os
import random
import re
import sys
from collections import defaultdict
class Node:
    nodeMap = defaultdict(lambda: None)
    @staticmethod
    def getNode(value):
        node = Node.nodeMap[value]
        if node:
            return node
        node = Node(value)
        Node.nodeMap[value] = node
        return node
    @staticmethod
    def addNode(parent, child):
        print(f'Parent is {parent.value}, Child is {child.value}')
        child.parent = parent
        parent.ownChildren.append(child)
        parent.addToOwnFamilyCount(child)
    @staticmethod
    def removeNode(parent, child):
        child.parent = None
        parent.ownChildren.remove(child)
        parent.subtractFromOwnFamilyCount(child)
    @staticmethod
    def getAllNodesAsList():
        return Node.nodeMap.values()
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.ownChildren = []
        self.allChildren = []
        self.ownFamilyCount = 1
    def addToOwnFamilyCount(self, node):
        print(f'Parent is {self.value}, Child is {node.value}: Adding child {node.ownFamilyCount} to parent {self.ownFamilyCount}')
        
        self.ownFamilyCount += node.ownFamilyCount
        if self.parent:
            self.parent.addToOwnFamilyCount(node)
    def subtractFromOwnFamilyCount(self, node):
        self.ownFamilyCount -= node.ownFamilyCount
        if self.parent:
            self.parent.subtractFromOwnFamilyCount(node)
        
# Complete the evenForest function below.
def evenForest(t_nodes, t_edges, t_from, t_to):
    print(f'tnodes {t_nodes}')
    print(f't_edges {t_edges}')
    print(f't_from {t_from}')
    print(f't_to {t_to}')
    for i in range(t_edges):
        parentNode = Node.getNode(t_to[i])
        childNode = Node.getNode(t_from[i])
        Node.addNode(parentNode,childNode)
    allNodes = Node.getAllNodesAsList()
    allEvenFamilies = 0
    for node in allNodes:
        if node.ownFamilyCount%2 == 0 and node.parent:
            allEvenFamilies +=1
            print(f'Node value: {node.value}, familyCount: {node.ownFamilyCount}')
    return allEvenFamilies
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t_nodes, t_edges = map(int, input().rstrip().split())

    t_from = [0] * t_edges
    t_to = [0] * t_edges

    for i in range(t_edges):
        t_from[i], t_to[i] = map(int, input().rstrip().split())

    res = evenForest(t_nodes, t_edges, t_from, t_to)

    fptr.write(str(res) + '\n')

    fptr.close()
