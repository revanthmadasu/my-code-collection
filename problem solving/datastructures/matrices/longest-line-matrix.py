'''
    problem: https://leetcode.com/problems/longest-line-of-consecutive-one-in-matrix
    concepts: Matrix, DFS
    performance: 39.58% runtime, 22.92% memory
    #todo: improve memory
'''
from typing import List
class Solution:
    def longestLine(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        lengthsMat = [[[-1,-1,-1,-1] for _ in range(n)] for _ in range(m)]
        def dfs(r, c, direction):
            # direction - 0-h, 1-v, 2-d, 3-ad
            if mat[r][c] == 0:
                lengthsMat[r][c] = [0,0,0,0]
                return 0
            elif lengthsMat[r][c][direction] != -1:
                return lengthsMat[r][c][direction]
            if direction == 0:
                hdir = 1
                if c+1 < n:
                    hdir +=  dfs(r,c+1,direction)
                lengthsMat[r][c][direction] = hdir
                return hdir
            if direction == 1:
                vdir = 1
                if r+1 < m:
                    vdir +=  dfs(r+1,c,direction)
                lengthsMat[r][c][direction] = vdir
                return vdir            
            if direction == 2:
                ddir = 1
                if c+1 < n and r+1 < m:
                    ddir +=  dfs(r+1,c+1,direction)
                lengthsMat[r][c][direction] = ddir
                return ddir
            if direction == 3:
                addir = 1
                if c-1 >= 0 and r+1 < m:
                    addir +=  dfs(r+1,c-1,direction)
                lengthsMat[r][c][direction] = addir
                return addir
        maxLen = 0
        for r in range(m):
            for c in range(n):
                if mat[r][c] == 1:
                    hdir = dfs(r,c,0)
                    vdir = dfs(r,c,1)
                    ddir = dfs(r,c,2)
                    addir = dfs(r,c,3)
                    maxLen = max(maxLen, hdir, vdir, ddir, addir)
        return maxLen
                    
                    
        