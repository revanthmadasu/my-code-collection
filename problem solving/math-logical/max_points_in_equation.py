'''
    problem: https://leetcode.com/problems/max-points-on-a-line
    concepts: math, backtracking
    4 testcases failing - using math equations. but some are failing because of rounding errors
'''
from typing import List

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 1:
            return len(points)
        
        def calcEquation(point1 ,point2):
            m = float('inf') if point2[0] == point1[0] else round((point2[1] - point1[1])/(point2[0] - point1[0]), 3)
            y_inter = round(point1[1] - m*point1[0], 2) if m!= float('inf') else None
            x_inter = round(point1[0], 3) if m == float('inf') else None
            return (m, y_inter, x_inter)
        equations = set()
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                equations.add(calcEquation(points[i], points[j]))
        maxCount = 0
        print(equations)
        for eq in equations:
            m, b, x_inter = eq
            eqCount = 0
            for point in points:
                if m == float('inf'):
                    if round(x_inter) == point[0]:
                        eqCount += 1
                else:
                    if point[1] == round(m*point[0] + b):
                        print(f'point {point} is in {eq}')
                        eqCount += 1
            if eqCount > maxCount:
                maxCount = eqCount
        return maxCount