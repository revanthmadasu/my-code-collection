'''
    Problem: https://leetcode.com/problems/rotting-oranges
    Concepts: bfs, matrix, disjointset, union-find
    performance: 5.11 runtime, 8.56 memory
    remark: worst implementation
    #todo: improve performance
'''
from collections import defaultdict
import math

def getHash(x,y):
    return ((x+y+1)*(x+y)/2)+y

def getPair(hashedVal):
    z = hashedVal
    w = math.floor((math.sqrt(8*z + 1)-1)/2)
    t = ((w*w)+w)/2
    y = z - t
    x = w - y
    return (x,y)

class DisjointSet:
    def __init__(self):
        self.valuesSetMap = defaultdict(lambda: None)
        self.allSets = []
    def makeSet(self, h_value, a_value):
        self.valuesSetMap[h_value] = {'hasRotton': a_value == 2, 'values': [h_value], 'rotten': {h_value} if a_value == 2 else set()}
        self.allSets.append(self.valuesSetMap[h_value])
    def findSet(self, value):
        return self.valuesSetMap[value]
    def union(self, val1, val2):
        valSet1 = self.valuesSetMap[val1]
        valSet2 = self.valuesSetMap[val2]
        merged = valSet1['values'] + valSet2['values']
        merged_rotten = valSet1['rotten'].union(valSet2['rotten'])
        mergedSet = {'hasRotton': valSet1['hasRotton'] or valSet2['hasRotton'], 'values': merged, 'rotten': merged_rotten}
        if valSet1 in self.allSets:
            self.allSets.remove(valSet1)
        if valSet2 in self.allSets: 
            self.allSets.remove(valSet2)
        self.allSets.append(mergedSet)
        for val in merged:
            self.valuesSetMap[val] = mergedSet
    def getAllSets(self):
        return self.allSets


class Solution:
    def orangesRotting(self, grid):
        disjointSet = DisjointSet()
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                val = grid[i][j]           
                cur_hash = getHash(i,j)
                if val != 0:
                    neighbours = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
                    eligible_neigh = []
                    for neigh in neighbours:
                        n_i, n_j = neigh
                        if n_i >= 0 and n_i < m and n_j >= 0 and n_j < n:
                            eligible_neigh.append((n_i, n_j))
                    completely_restricted = True
                    for neigh in eligible_neigh:
                        n_i, n_j = neigh
                        if grid[n_i][n_j] != 0:
                            completely_restricted = False
                    if completely_restricted and val == 1:
                        return -1
                    disjointSet.makeSet(cur_hash, val)
                    if i-1 >= 0:
                        row_neigh_hash = getHash(i-1,j)
                        if disjointSet.findSet(row_neigh_hash):
                            disjointSet.union(cur_hash, row_neigh_hash)
                    if j-1 >= 0:
                        col_neigh_hash = getHash(i, j-1)
                        if disjointSet.findSet(col_neigh_hash):
                            disjointSet.union(cur_hash, col_neigh_hash)
        rot_counts = []
        for neigh_set in disjointSet.allSets:
            if not neigh_set['hasRotton']:
                return -1
        # print(f'all sets: {disjointSet.allSets}')
        for neigh_set in disjointSet.allSets:
            rot_counts.append(self.getRotCount(neigh_set, m, n))
        if len(rot_counts):
            return max(rot_counts)-1
        return 0
    def getRotCount(self, group, m, n):
        # all_pairs_count = len(group['values'])
        # rotten_count = len(group['rotten'])
        # all_pairs = list(map(lambda h: getPair(h), group['values']))
        # rotten_pairs = list(map(lambda h: getPair(h), group['rotten']))
        # print(f'all pairs are {all_pairs}')
        # print(f'rotten pairs are {rotten_pairs}')
        rot_map = defaultdict(lambda: None)
        for val in group['values']:
            rot_map[val] = False
        for val in group['rotten']:
            rot_map[val] = True
        # print(f'rot map is {rot_map}')
        cur_rotten = group['rotten']
        time_counter = 0
        while len(cur_rotten):
            time_counter += 1
            new_rot = []
            for rot_val in cur_rotten:
                i,j = getPair(rot_val)
                print(f'currently at {i,j}')
                neighbours = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
                # print(f'neighs are {neighbours}')
                rot_neigh = []
                for neigh in neighbours:
                    n_i, n_j = neigh
                    if n_i >= 0 and n_i < m and n_j >= 0 and n_j < n:
                        # eligible_neighbours.append(neigh)
                        n_hash = getHash(n_i, n_j)
                        if n_hash in rot_map:
                            # print(f'{getPair(n_hash)} exists')
                            if rot_map[n_hash] == False:
                                # print(f'{getPair(n_hash)} is rotting')
                                rot_map[n_hash] = True
                                rot_neigh.append(n_hash)
                                # print(f'new rot pos: {getPair(n_hash)}')
                            # else: 
                            #     print(f'{getPair(n_hash)} already rotten')
                        # else:
                        #     print(f'{getPair(n_hash)} not in rot map')
                new_rot.extend(rot_neigh)
                rot_neigh_pairs = list(map(lambda h: getPair(h), rot_neigh))
                print(f'new rots for current node are {rot_neigh_pairs}')
            new_rot_pairs = list(map(lambda h: getPair(h), new_rot))
            print(f'new rots are {new_rot_pairs}')
            cur_rotten = new_rot
        return time_counter

grid = [[2,0,0,2,1,2,2,2,2,1],[1,2,0,0,1,1,1,1,2,1],[1,2,1,1,1,1,2,0,1,0],[2,2,1,2,0,1,1,2,2,0],[1,1,0,0,0,2,1,2,2,0],[0,1,1,1,0,2,2,2,0,1],[2,2,1,0,2,0,2,1,1,1]]
# time limit exceeds
# grid = [
#     [1,0,1,0,1,0,1,1,0],
#     [0,0,0,1,2,2,2,0,2],
#     [2,2,1,1,2,2,0,0,0],
#     [1,2,0,0,2,2,1,1,1],
#     [0,1,1,2,1,1,2,2,2],
#     [2,1,2,0,2,1,1,2,2],
#     [1,2,1,0,2,1,1,2,2],
#     [0,0,2,1,1,2,2,2,0],
#     [1,2,0,2,1,0,2,0,0]]
print(Solution().orangesRotting(grid))