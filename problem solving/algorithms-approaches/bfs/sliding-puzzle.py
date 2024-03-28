'''
    problem: https://leetcode.com/problems/sliding-puzzle
    concepts: Array, BFS
    performance: 85.31% runtime, 51.16% memory
'''
from typing import List
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        recordedMoves = set()
        target = (1,2,3,4,5,0)
        def matToTuple(mat):
            t = tuple()
            z = None
            for i, row in enumerate(mat):
                for j, col in enumerate(row):
                    if col == 0:
                        z = i*3 + j
                    t = t + (col, )
            return (t, z)
        cur, zPos = matToTuple(board)
        if cur == target:
            return 0
        recordedMoves.add(cur)
        numMoves = 0
        queue = [(cur, zPos)]
        while len(queue):
            newQueue = []
            numMoves += 1
            for qItem in queue:
                boardT, z = qItem
                boardL = list(boardT)
                # up is possible
                if z//3 > 0:
                    boardUp = boardL.copy()
                    boardUp[z-3], boardUp[z] = boardUp[z], boardUp[z-3]
                    boardUpT = tuple(boardUp)
                    if boardUpT == target:
                        return numMoves
                    if boardUpT not in recordedMoves:
                        newQueue.append((boardUpT, z-3))
                    recordedMoves.add(boardUpT)
                # down
                if z // 3 == 0:
                    boardDown = boardL.copy()
                    boardDown[z+3], boardDown[z] = boardDown[z], boardDown[z+3]
                    boardDownT = tuple(boardDown)
                    if boardDownT == target:
                        return numMoves
                    if boardDownT not in recordedMoves:
                        newQueue.append((boardDownT, z+3))
                    recordedMoves.add(boardDownT)
                    
                # left
                if z % 3 > 0:
                    boardLeft = boardL.copy()
                    boardLeft[z-1], boardLeft[z] = boardLeft[z], boardLeft[z-1]
                    boardLeftT = tuple(boardLeft)
                    if boardLeftT == target:
                        return numMoves
                    if boardLeftT not in recordedMoves:
                        newQueue.append((boardLeftT, z-1))
                    recordedMoves.add(boardLeftT)
                        
                # right
                if z % 3 < 2:
                    boardRight = boardL.copy()
                    boardRight[z+1], boardRight[z] = boardRight[z], boardRight[z+1]
                    boardRightT = tuple(boardRight)
                    if boardRightT == target:
                        return numMoves
                    if boardRightT not in recordedMoves:
                        newQueue.append((boardRightT, z+1))
                    recordedMoves.add(boardRightT)
                        
            queue = newQueue
        return -1