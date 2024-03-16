'''
    problem: https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons
    concepts: intervals
    performance: 5% runtime, 88.73% memory
'''
from typing import List
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        intersections = []
        i = 0
        points.sort()
        def getIntersection(point1, point2):
            # print(f'intersection of {point1}, {point2}: ')
            intersection = (max(point1[0], point2[0]), min(point1[1], point2[1]))
            if intersection[0] <= intersection[1] and intersection[0] >= point1[0] and intersection[0] >= point2[0] and intersection[1] <= point1[1] and intersection[1] <= point2[1]:
                print(f'is {intersection}')
                return intersection
            # print('not intersecting')
            return None
        while i < len(points):
            cur = points[i]
            if i+1 < len(points):
                next_cur = getIntersection(cur, points[i+1])
            while i+1 < len(points) and next_cur:
                cur = next_cur
                i += 1
                if i+1 < len(points):
                    next_cur = getIntersection(cur, points[i+1])
            i += 1
            intersections.append(cur)
        # print(intersections)
        return len(intersections)
        