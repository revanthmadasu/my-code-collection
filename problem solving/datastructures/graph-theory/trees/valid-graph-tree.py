'''
    problem: https://leetcode.com/problems/graph-valid-tree
    concepts: tree, graph, dfs, recursion
    performance: 49.86% runtime, 22.86% memory
'''
from typing import List
class Node:
    def __init__(self, val):
        self.val = val
        self.neighbours = set()
        self.isVisited = False
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n-1 != len(edges):
            return False
        allNodes = [Node(i) for i in range(n)]
        for edge in edges:
            node1 = allNodes[edge[0]-1]
            node2 = allNodes[edge[1]-1]
            if (node1 in node2.neighbours) or (node2 in node1.neighbours):
                return False
            node1.neighbours.add(node2)
            node2.neighbours.add(node1)
        queue = allNodes[0]
        def dfs(node, prevNode):
            if not node:
                return True
            if node.isVisited:
                return False
            # print(f'visiting {node.val}')
            node.isVisited = True

            for neighNode in node.neighbours:
                if neighNode != prevNode:
                    if neighNode.isVisited:
                        return False
                    if not dfs(neighNode, node):
                        return False
            return True
        return dfs(allNodes[0], None)
