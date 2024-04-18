'''
    Problem: https://leetcode.com/problems/k-closest-points-to-origin/
    Concepts: Sorting, Array
    performance: 95.53% runtime, 74.16% memory
'''
from typing import List
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = [(point[0]**2 + point[1]**2)**(0.5) for point in points]
        indices = list(range(len(points)))
        indices.sort(key=lambda i: distances[i])
        return [points[i] for i in indices[:k]]