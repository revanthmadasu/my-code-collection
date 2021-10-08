#!/bin/python3
# https://www.hackerrank.com/challenges/the-quickest-way-up/problem
import math
import os
import random
import re
import sys
from collections import defaultdict
import bisect
class Node:
    sources = set()
    destinations = set()
    nodesMap = defaultdict(lambda: None)
    costMap = defaultdict(lambda: None)
    @staticmethod
    def getNode(vertex):
        if Node.nodesMap[vertex] == None:
            Node.nodesMap[vertex] = Node(vertex)
            # print('creating node:', vertex)
        return Node.nodesMap[vertex]
    @staticmethod
    def nodeExists(vertex):
        return Node.nodesMap[vertex]
    @staticmethod
    def getCostMap(vertex):
        if Node.costMap[vertex] == None:
            Node.costMap[vertex] = defaultdict(lambda: None)
        return Node.costMap[vertex]
    @staticmethod
    def connect(source, destination, cost = 0, jumpNode = False):
        # print('adding destination ',destination.vertex)
        if jumpNode:
            if source.vertex < destination.vertex:
                source.isLadder = True
            else:
                source.isSnake = True
        source.destinations.append(destination)
        destination.sources.append(source)

        Node.sources.add(source)
        Node.destinations.add(destination)

        sourceCostMap = Node.getCostMap(source.vertex)
        sourceCostMap[destination.vertex] = cost
    @staticmethod
    def minimumMoves(source, destination):
        # print(f'Generating minimum moves from {source.vertex} to {destination.vertex}')
        sourceVertex = source.vertex
        destinationVertex = destination.vertex
        numOfMoves = 0
        currentPos = sourceVertex
        while True:
            maxNumOfSteps = 6 if destinationVertex - currentPos > 6 else destinationVertex - currentPos
            notPossible = False
            for step in range(maxNumOfSteps, 0, -1):
                node = Node.nodeExists(currentPos + step)
                if source.vertex == 90:
                    print(f'node for {currentPos + step}: {node}')
                if node:
                    if (node.isLadder or node.isSnake) and node != destination:
                        print(f'not possible to go to {node.vertex}')
                        notPossible = True
                        continue
                currentPos = currentPos + step
                numOfMoves += 1
                notPossible = False
                break
            if notPossible:
                return -1
            if currentPos == destinationVertex:
                break
        return numOfMoves
    @staticmethod
    def clear():
        Node.sources = set()
        Node.destinations = set()
        Node.nodesMap = defaultdict(lambda: None)
        Node.costMap = defaultdict(lambda: None)

    def __init__(self,vertex):
        self.vertex = vertex
        self.sources = []
        self.destinations = []
        self.costMap = Node.getCostMap(vertex)
        self.costMap[vertex] = 0
        self.isLadder = False
        self.isSnake = False
    
def nextSources(node):
    vertex = node.vertex
    print(f'Generating next sources for vertex: {vertex}')
    allSources = sorted([source for source in list(Node.sources) if (source.isLadder or source.isSnake) and source.vertex > vertex], key=lambda item: item.vertex)
    if len(allSources):
        allSourceVertices = list(map(lambda x: x.vertex, allSources))
        allLadders = [source for source in allSources if source.isLadder]
        if len(allLadders):
            nextImmediateLadder = allLadders[0]
            nextImmediateLadderIndex = allSources.index(nextImmediateLadder)
            nextImmediateLadderDest = nextImmediateLadder.destinations[0]
            nextImmediateLadderDestVertex = nextImmediateLadderDest.vertex
            nextImmediateLadderDestIndex = bisect.bisect(allSourceVertices,nextImmediateLadderDest.vertex) - 1
            possibleSources = [source for source in allSources[nextImmediateLadderIndex:nextImmediateLadderDestIndex+1] if source.destinations[0].vertex >= nextImmediateLadderDestVertex]
            possibleSources = [source for source in allSources if source.destinations[0].vertex >= nextImmediateLadderDestVertex]
        # print(f'Next immediate source: {nextImmediateLadder.vertex}\nNext immediate dest for source: {nextImmediateLadderDestVertex}')
            print(f'Possible sources: {list(map(lambda source: source.vertex, possibleSources))}')
            return possibleSources
        else:
            print(f'Returning all sources: {list(map(lambda source: source.vertex, allSources))}')
            allSources.append(Node.getNode(100))
            return allSources
        # nextImmediateSourceIndex = bisect.bisect(allSourceVertices,vertex)


        # nextImmediateSource = allSources[nextImmediateSourceIndex]
        # nextImmediateLSourceDest = nextImmediateSource.destinations[0]
        # nextImmediateLSourceDestVertex = nextImmediateLSourceDest.vertex
        # nextImmediateSourceDestIndex = bisect.bisect(allSourceVertices,nextImmediateLSourceDest.vertex) - 1
        # print(f'Next immediate source: {nextImmediateSource.vertex}\nNext immediate dest for source: {nextImmediateLSourceDest.vertex}')
        # possibleSources = [source for source in allSources[nextImmediateSourceIndex:nextImmediateSourceDestIndex+1] if source.destinations[0].vertex >= nextImmediateLSourceDestVertex]
        # if len(possibleSources):
        #     return possibleSources
    print(f'Returning Node 100')
    return [Node.getNode(100)]

def dfs(node):
    if node.vertex == 100:
        print('Destination reached : ',end='')
        return True
    costMap = Node.getCostMap(1)
    currentNodeCostMap = node.costMap
    currentVertex = node.vertex
    allDests = list(map(lambda item: item.vertex,sorted(node.destinations, key = lambda dest: dest.vertex)))
    # print(f'current node: {currentVertex}  dests: {allDests}')
    for destNode in node.destinations:
        destNodeVertex = destNode.vertex
        if costMap[destNodeVertex] == None:
            cost = currentNodeCostMap[destNodeVertex] + costMap[currentVertex]
            costMap[destNodeVertex] = cost
            if dfs(destNode):
                print(f'{destNode.vertex} <-', end = '')
        else:
            # print(f'current vertex: {currentVertex} costMap: {costMap}')
            cost = currentNodeCostMap[destNodeVertex] + costMap[currentVertex]
            if costMap[destNodeVertex] >= cost:
                costMap[destNodeVertex] = cost
                if dfs(destNode):
                    print(f'{destNode.vertex} <-', end = '')
            else:
                continue
# Complete the quickestWayUp function below.
def quickestWayUp(ladders, snakes):
    Node.clear()
    allSources = sorted(Node.sources, key = lambda item: item.vertex)
    allDests = sorted(Node.destinations, key = lambda dest: dest.vertex)
    print(f'Next Test Case. allSources: {allSources}    allDests: {allDests}')
    for ladder in ladders:
        src = Node.getNode(ladder[0])
        dest = Node.getNode(ladder[1])
        Node.connect(src, dest, 0, True)
        # print(f"connecting to {dest.vertex} block1")
    for snake in snakes:
        src = Node.getNode(snake[0])
        dest = Node.getNode(snake[1])
        Node.connect(src, dest, 0, True)
        # print(f"connecting to {dest.vertex} block2")

    Node.sources.add(Node.getNode(100))
    Node.destinations.add(Node.getNode(1))
    allSources = sorted(Node.sources, key = lambda item: item.vertex)
    allDests = sorted(Node.destinations, key = lambda dest: dest.vertex)
    for dest in allDests:
        possibleNextPoints = nextSources(dest)
        # print(dest.vertex, f'next points: {possibleNextPoints}')
        for nextPoint in possibleNextPoints:
            cost = Node.minimumMoves(dest, nextPoint)
            print(f'Cost from {dest.vertex} to {nextPoint.vertex} is {cost}')
            if cost != -1:
                Node.connect(dest,nextPoint, cost)
                # print(f"connecting to {dest.vertex} block3")
    print(f'before dfs: {Node.getCostMap(1)}')
    dfs(Node.getNode(1))
    print(Node.getCostMap(1)[100])
    print(f'after dfs: {Node.getCostMap(1)}')
    return Node.getCostMap(1)[100] or -1
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        ladders = []

        for _ in range(n):
            ladders.append(list(map(int, input().rstrip().split())))

        m = int(input())

        snakes = []

        for _ in range(m):
            snakes.append(list(map(int, input().rstrip().split())))

        result = quickestWayUp(ladders, snakes)

        fptr.write(str(result) + '\n')

    fptr.close()