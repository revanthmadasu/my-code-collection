'''
    Problem: https://leetcode.com/problems/parallel-courses/
    Concepts: Topological Sort, Graph, DFS
    performance: 36.29% runtime, 6.08% memory
    #todo: improve performance - try with DP
'''
from typing import List
class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        req = {i: set() for i in range(n)}
        for rel in relations:
            req[rel[1]-1].add(rel[0]-1)
        curPath = dict()
        visitedRes = dict()
        def dfs(c):
            if c in curPath and curPath[c]:
                return -1
            if c in visitedRes:
                return visitedRes[c]
            if len(req[c]) == 0:
                visitedRes[c] = 1
                return 1
            curPath[c] = True
            resList = []
            for nextC in req[c]:
                res = dfs(nextC)
                if res == -1:
                    return -1
                resList.append(res)
            curPath[c] = False
            
            res = max(resList) + 1
            visitedRes[c] = res
            return res
        maxRes = 0
        for i in range(n):
            res = dfs(i)
            if res == -1:
                return -1
            maxRes = max(res, maxRes)
        return maxRes

# Concepts: BFS, Graph
# performance: 20.54% runtime, 6.08% memory
# class Solution:
#     def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
#         req = {i: set() for i in range(n)}
#         allows = {i: set() for i in range(n)}
#         # print(allows)
#         for rel in relations:
#             req[rel[0]-1].add(rel[1]-1)
#             allows[rel[1]-1].add(rel[0]-1)
#         semCourses = [c for c in req if len(req[c]) == 0]
#         semCount = 0
#         doneCourses = set()
#         while semCourses:
#             semCount += 1
#             for course in semCourses:
#                 doneCourses.add(course)
#             nextCourses = []
#             for doneCourse in semCourses:
#                 for pendingCourse in allows[doneCourse]:
#                     if pendingCourse in doneCourses:
#                         continue
#                     possible = True
#                     for reqCourse in req[pendingCourse]:
#                         if reqCourse not in doneCourses:
#                             possible = False
#                             break
#                     if possible:
#                         nextCourses.append(pendingCourse)
#             semCourses = nextCourses
#         return semCount if len(doneCourses) == n else -1
