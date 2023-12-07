'''
    problem: https://leetcode.com/problems/evaluate-division
    concepts: Graphs, graph traversal, cost, Union find, disjoint set
    performance: 74.97% runtime, 18.70% memory
    todo: improve on memory. try without union find or include union find in the graph itself
'''
from typing import List
from collections import defaultdict
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        eq_len = len(equations)
        graph = Graph()
        disjointset = DisjointSet()
        for i in range(eq_len):
            graph.connectNodes(graph.getNode(equations[i][0]).val, graph.getNode(equations[i][1]).val, values[i])
            disjointset.getSet(equations[i][0])
            disjointset.getSet(equations[i][1])
            disjointset.union(equations[i][0], equations[i][1])
        res = []
        for query in queries:
            inVal, outVal = query
            inSet = disjointset.findSet(inVal)
            outSet = disjointset.findSet(outVal)
            if (not inSet) or (not outSet) or (not outVal in inSet):
                res.append(-1)
                continue
            else:
                res.append(graph.getCost(inVal, outVal))
        return res
            
class Node:
    def __init__(self, val):
        self.val = val
        self.neighbours = set()
        self.costs = defaultdict(lambda: None)
    # direction 0: out: self -> neighbour, 1: in: self <- neighbour
    def connect(self, neighbourNode, direction, cost):
        if direction == 0:
            inNode = self
            outNode = neighbourNode
        else:
            inNode = neighbourNode
            outNode = self
        inNode.costs[outNode.val] = cost
        outNode.costs[inNode.val] = 1/cost
        inNode.neighbours.add(outNode)
        outNode.neighbours.add(inNode)




class Graph:
    def __init__(self):
        self.allNodes = set()
        self.nodesDict = defaultdict(lambda: None)
        self.visited = defaultdict(lambda: False)
    def getNode(self, val):
        if not self.nodesDict[val]:
            node = Node(val)
            self.allNodes.add(node)
            self.nodesDict[val] = node     
        return self.nodesDict[val]
    def connectNodes(self, inNodeVal, outNodeVal, cost):
        inNode = self.nodesDict[inNodeVal]
        outNode = self.nodesDict[outNodeVal]
        inNode.connect(outNode, 0, cost)
    def getCost(self, node1Val, node2Val):
        node1 = self.nodesDict[node1Val]
        node2 = self.nodesDict[node2Val]
        if not node1.costs[node2Val]:
            self.visited = defaultdict(lambda: False)
            return self.getCostRecursively(node1, node2Val)
        else:
            return node1.costs[node2Val]
    def getCostRecursively(self, currNode, targetNodeVal, acc = 1):
        self.visited[currNode.val] = True
        if currNode.val == targetNodeVal:
            return acc
        res = -1
        for neigh in currNode.neighbours:
            if not self.visited[neigh.val]:
                res = self.getCostRecursively(neigh, targetNodeVal, acc*currNode.costs[neigh.val])
                if res != -1:
                    break
        return res
                

class DisjointSet:
    def __init__(self):
        self.valuesSetMap = defaultdict(lambda: None)
        self.allSets = []
    def getSet(self, val):
        if not self.valuesSetMap[val]:
            self.makeSet(val)
        return self.valuesSetMap[val]
    def makeSet(self, val):
        self.valuesSetMap[val] = set([val])
        self.allSets.append(self.valuesSetMap[val])
    def findSet(self, value):
        return self.valuesSetMap[value]
    def union(self, val1, val2):
        valSet1 = self.valuesSetMap[val1]
        valSet2 = self.valuesSetMap[val2]
        merged = valSet1.union(valSet2)
        if valSet1 in self.allSets:
            self.allSets.remove(valSet1)
        if valSet2 and (valSet2 in self.allSets): 
            self.allSets.remove(valSet2)
        self.allSets.append(merged)
        for val in merged:
            self.valuesSetMap[val] = merged
    def getAllSets(self):
        return self.allSets


sol = Solution()

print(sol.calcEquation([["a","b"],["b","c"]],[2.0,3.0], [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]))