'''
    problem: https://leetcode.com/problems/minimum-area-rectangle
    concepts: Hashtable
    performance: 8.36% runtime, 14.75% memory
    #todo: improve performance
'''
'''
x-map - y points for given x
1:[1,3]
3:[1,3]
4:[1,3]

y-map: - x points for given y
1:[1,3,4]
3:[1,3,4]
'''
from typing import List
class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        xmap = dict()
        ymap = dict()
        for point in points:
            if point[0] not in xmap:
                xmap[point[0]] = set()
            xmap[point[0]].add(point[1])
            if point[1] not in ymap:
                ymap[point[1]] = set()
            ymap[point[1]].add(point[0])
        minArea = float('inf')
        for point in points:
            x1 = point[0]
            y1 = point[1]
            x1_ys = xmap[x1].copy()
            x1_ys.remove(y1)
            y1_xs = ymap[y1].copy()
            y1_xs.remove(x1)
            for y2 in x1_ys:
                y2_xs = ymap[y2].copy()
                y2_xs.remove(x1)
                x2s = y1_xs.intersection(y2_xs)
                ydiff = abs(y2-y1)
                for x2 in x2s:
                    xdiff = abs(x2-x1)
                    minArea = min(minArea, ydiff*xdiff)
        return 0 if minArea == float('inf') else minArea
                    