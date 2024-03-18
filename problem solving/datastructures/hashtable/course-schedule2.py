'''
    problem: https://leetcode.com/problems/course-schedule-ii/
    concepts: hashtable, graph
    performance: 99.37% runtime, 46.33% memory
'''
from typing import List
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # prereqReqMap = dict()
        prereqReqCounts = [0] * numCourses
        coursesDepOnPrereq = dict()
        for prereq in prerequisites:
            prereqReqCounts[prereq[0]] += 1
            
            if prereq[1] not in coursesDepOnPrereq:
                coursesDepOnPrereq[prereq[1]] = [prereq[0]]
            else:
                coursesDepOnPrereq[prereq[1]].append(prereq[0])

        # print(f'courses dep on prereq: {coursesDepOnPrereq}')
        seq = [courseNum for courseNum in range(numCourses) if not prereqReqCounts[courseNum]]
        queue = seq
        while len(queue) and len(seq) != numCourses:
            # print(f'queue is {queue}')
            newQueue = []
            for availableCourseNum in queue:
                # print(f'available course: {availableCourseNum}')
                if availableCourseNum in coursesDepOnPrereq:
                    for dependentCourse in coursesDepOnPrereq[availableCourseNum]:
                        if prereqReqCounts[dependentCourse] <= 1:
                            newQueue.append(dependentCourse)
                        prereqReqCounts[dependentCourse] -= 1
            seq.extend(newQueue)
            queue = newQueue
        return seq if len(seq) == numCourses else []