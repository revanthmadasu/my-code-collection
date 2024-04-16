'''
    problem: https://leetcode.com/problems/cut-off-trees-for-golf-event/
    concepts: BFS, Heap
    #incomplete: time limit exceeded - 33/55 testcases passed
    #todo: complete it - try running multi source shortest path algorithm first to get distances instead of bfs
'''
from heapq import heappop, heappush
from typing import List
from itertools import product
from collections import deque
class Solution:

    def cutOffTree(self, forest: List[List[int]]) -> int:

        def bfs(beg, end):
            queue, uns = deque([(beg,0)]), unseen.copy()
            uns.discard(beg)

            while queue:
                (r,c), steps = queue.popleft()

                if (r,c) == end: return steps

                for R,C in ((r-1,c), (r,c-1), (r+1,c), (r,c+1)):

                    if (R,C) not in uns: continue

                    queue.append(((R,C),steps+1))
                    uns.discard((R,C))

            return -1
        
        m, n, ans = len(forest), len(forest[0]), 0
        start, trees = (0,0), []

        grid = tuple(product(range(m), range(n)))
        print(grid)
        unseen = set(filter(lambda x: forest[x[0]][x[1]] != 0, grid))

        for r,c  in grid:
            if forest[r][c] > 1: heappush(trees,(forest[r][c], (r,c)))

        while trees:
            if (res:= bfs(start,(pos:= heappop(trees)[1]))) < 0: return -1

            ans += res
            start = pos

        return ans

sol = Solution()
print(sol.cutOffTree([[1,2,3],[0,0,4],[7,6,5]]))
# class Solution:
#     def cutOffTree(self, forest: List[List[int]]) -> int:
#         m = len(forest)
#         n = len(forest[0])
#         minHeap = [] # (height, (i,j))
#         heapq.heapify(minHeap)
#         for r in range(m):
#             for c in range(n):
#                 if forest[r][c] != 0:
#                     heapq.heappush(minHeap, (forest[r][c], (r,c)))
#         def getMinDistance(srcPos, dstPos):
#             q = [srcPos]
#             dist = 0
#             visited = dict()
#             while q:
#                 # print(f'cur q: {}')
#                 newQ = []
#                 for pos in q:
#                     visited[pos] = True
#                     if forest[pos[0]][pos[1]] == 0:
#                         continue
#                     if pos == dstPos:
#                         return dist
#                     else:
#                         nextPos = [(pos[0]+1, pos[1]), (pos[0], pos[1]+1), (pos[0]-1, pos[1]), (pos[0], pos[1]-1)]
#                         nextPos = [npos for npos in nextPos if npos[0] >= 0 and npos[0] < m and npos[1] >= 0 and npos[1] < n and npos not in visited]
#                         newQ.extend(nextPos)
#                 q = newQ
#                 dist += 1
#             return -1
#         dist = 0
#         curPos = (0,0)
#         while len(minHeap):
#             treeHeight, pos = heapq.heappop(minHeap)
#             distToNextPos = getMinDistance(curPos, pos)
#             if distToNextPos == -1:
#                 return -1
#             dist += distToNextPos
#             curPos = pos
#         if len(minHeap):
#             return -1
#         return dist
