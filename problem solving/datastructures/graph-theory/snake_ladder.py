'''
    problem: https://leetcode.com/problems/snakes-and-ladders
    concepts: bfs, graphs
    performance: 6.44% runtime, 7.54% memory
    #todo: improve performance - try bfs directly on matrix instead of graphs
'''
from collections import defaultdict
class Solution(object):
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        graph = Graph()
        # m rows, n cols
        m = len(board)
        n = len(board[0])
        all_nodes_size = m*n
        for i_node in range(all_nodes_size):
            graph.getNode(i_node + 1)
        for i in range(m):
            row = m-1-i
            for j in range(n):
                col = j if row%2 == 0 else n-1 - j
                nodeVal = (row*n) + col +1
                # print(f'nodeval: {nodeVal}')
                graph.getNode(nodeVal).skip = board[i][j]
                # print(f'dice connect for {nodeVal}')
                for dice_res in range(nodeVal+1, min(nodeVal+7, all_nodes_size+1)):
                    graph.connectNodes(nodeVal, dice_res, 1)
        return graph.bfs(1, m*n)

class Node:
    def __init__(self, val, skip = -1):
        self.val = val
        self.neighbours = set()
        self.costs = defaultdict(lambda: None)
        self.skip = skip
    # direction 0: out: self -> neighbour, 1: in: self <- neighbour
    def connect(self, neighbourNode, cost):
        self.costs[neighbourNode.val] = cost
        # print(f'connecting {self.val} -> {neighbourNode.val}')
        self.neighbours.add(neighbourNode)




class Graph:
    def __init__(self):
        self.allNodes = set()
        self.nodesDict = defaultdict(lambda: None)
        self.visited = defaultdict(lambda: False)
    def getNode(self, val, skip = -1):
        if not self.nodesDict[val]:
            node = Node(val, skip)
            self.allNodes.add(node)
            self.nodesDict[val] = node     
        return self.nodesDict[val]
    def connectNodes(self, inNodeVal, outNodeVal, cost):
        inNode = self.nodesDict[inNodeVal]
        outNode = self.nodesDict[outNodeVal]
        inNode.connect(outNode, cost)

    def bfs(self, startNodeVal, targetNodeVal):
        visited = defaultdict(lambda: False)
        startNode = self.getNode(1)
        queue = [startNode]
        i = 0
        possible = False
        while len(queue):
            print(f'================iteration {i}==================')
            new_queue = []
            for node in queue:
                if visited[node.val]:
                    continue
                else:
                    start_node = node
                    skip = False
                    print(f'visiting: {node.val}')
                    if node.skip != -1:
                        node = self.nodesDict[node.skip]
                        print(f'skipped to : {node.val}')
                        skip = True

                    if node.val == targetNodeVal:
                        possible = True
                        break
                    if (not visited[node.val]) or skip:
                        for neigh_node in node.neighbours:
                            if not visited[neigh_node.val]:
                                new_queue.append(neigh_node)
                    visited[start_node.val] = True
            if possible:
                break
            queue = new_queue
            i += 1
        return -1 if not possible else i
sol = Solution()
board1 = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
board2 = [[-1,-1],[-1,3]]
board3 = [
    [-1,-1,-1,-1,48,5,-1],# 43 44 45 46 47 48 49
    [12,29,13,9,-1,2,32],# 42 41 40 39 38 37 36
    [-1,-1,21,7,-1,12,49],# 29 30 31 32 33 34 35
    [42,37,21,40,-1,22,12],# 28 27 26 25 24 23 22
    [42,-1,2,-1,-1,-1,6],# 15 16 17 18 19 20 21
    [39,-1,35,-1,-1,39,-1],# 14 13 12 11 10 9 8
    [-1,36,-1,-1,-1,-1,5]] # 1 2 3 4 5 6 7
# sol: 1 => 2->36 => 41->29 => 35->49
board4 = [[-1,-1],[-1,4]]
board5 = [
    [-1,-1,-1,46,47,-1,-1,-1],# 64 63 62 61 60 59 58 57
    [51,-1,-1,63,-1,31,21,-1],# 49 50 51 52 53 54 55 56
    [-1,-1,26,-1,-1,38,-1,-1],# 48 47 46 45 44 43 42 41
    [-1,-1,11,-1,14,23,56,57],# 33 34 35 36 37 38 39 40
    [11,-1,-1,-1,49,36,-1,48],# 32 31 30 29 28 27 26 25
    [-1,-1,-1,33,56,-1,57,21],# 17 18 19 20 21 22 23 24
    [-1,-1,-1,-1,-1,-1,2,-1], # 16 15 14 13 12 11 10  9
    [-1,-1,-1,8,3,-1,6,56]]   #  1  2  3  4  5  6  7  8
board6 = [
    [-1,1,1,1], # 16 15 14 13
    [-1,7,1,1], #  9 10 11 12
    [16,1,1,1], #  8  7  6  5
    [-1,1,9,1]  #  1  2  3  4
]
# sol: 1 => 3->9 => 10->7 => 8->16
# print(sol.snakesAndLadders(board1))
# print(sol.snakesAndLadders(board2))
# print(sol.snakesAndLadders(board3))
# print(sol.snakesAndLadders(board5))
print(sol.snakesAndLadders(board6))