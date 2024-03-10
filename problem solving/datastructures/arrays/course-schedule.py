'''
    problem: https://leetcode.com/problems/course-schedule
    concepts: arrays
    performance: 5% runtime, 60.93% memory
    #todo - improve runtime. worst way of implimentation
'''
from typing import List
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # prerequisites -> [course, prereq]
        # dependents[prereq] = [courses]
        dependents = []
        # required[course] = [prereqs]
        required = []
        for i in range(numCourses):
            dependents.append([])
            required.append([])
        coursesCompleted = [False] * numCourses
        for prereqItem in prerequisites:
            prereq = prereqItem[1]
            course = prereqItem[0]
            dependents[prereq].append(course)
            required[course].append(prereq)

        completedCourses = set([i for i in range(numCourses) if len(required[i]) == 0])
        for i in completedCourses:
            coursesCompleted[i] = True
        prevLen = 0
        # print(f'Completed courses: {completedCourses}, {required}')
        while prevLen != len(completedCourses):
            # print(f'Completed courses: {completedCourses}')
            
            prevLen = len(completedCourses)
            newCourses = []
            for completedCourseIndex in completedCourses:
                for dependentCourse in dependents[completedCourseIndex]:
                    if all([coursesCompleted[i] for i in required[dependentCourse]]):
                        coursesCompleted[dependentCourse] = True
                        newCourses.append(dependentCourse)
            if len(newCourses):
                for newCourse in newCourses:
                    completedCourses.add(newCourse)
        return len([courseCompleted for courseCompleted in coursesCompleted if courseCompleted]) >= numCourses
