'''
    Problem: https://leetcode.com/problems/parallel-courses/
    Concepts: BFS, Graph
    performance: 20.54% runtime, 6.08% memory
    #todo: improve performance - try with topological sorting, directed acyclic graph
'''
from typing import List
class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        req = {i: set() for i in range(n)}
        allows = {i: set() for i in range(n)}
        # print(allows)
        for rel in relations:
            req[rel[0]-1].add(rel[1]-1)
            allows[rel[1]-1].add(rel[0]-1)
        semCourses = [c for c in req if len(req[c]) == 0]
        semCount = 0
        doneCourses = set()
        while semCourses:
            semCount += 1
            for course in semCourses:
                doneCourses.add(course)
            nextCourses = []
            for doneCourse in semCourses:
                for pendingCourse in allows[doneCourse]:
                    if pendingCourse in doneCourses:
                        continue
                    possible = True
                    for reqCourse in req[pendingCourse]:
                        if reqCourse not in doneCourses:
                            possible = False
                            break
                    if possible:
                        nextCourses.append(pendingCourse)
            semCourses = nextCourses
        return semCount if len(doneCourses) == n else -1
