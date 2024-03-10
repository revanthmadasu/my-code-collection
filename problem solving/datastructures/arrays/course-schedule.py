'''
    problem: https://leetcode.com/problems/course-schedule
    concepts: arrays
    performance: 64.90% runtime, 83.97% memory
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
        for prereqItem in prerequisites:
            prereq = prereqItem[1]
            course = prereqItem[0]
            dependents[prereq].append(course)
            required[course].append(prereq)

        coursesCompleted = [len(required[i]) == 0 for i in range(numCourses)]
        # print(f'Completed courses: {completedCourses}, {required}')
        newCompletedCourses = [i for i in range(numCourses) if coursesCompleted[i]]
        while len(newCompletedCourses):
            # print(f'Completed courses: {completedCourses}')
            
            # print(f'newCompletedCourses is {newCompletedCourses}')
            nextNew = set()
            for completedCourseIndex in newCompletedCourses:
                for dependentCourse in dependents[completedCourseIndex]:
                    if all([coursesCompleted[i] for i in required[dependentCourse]]):
                        coursesCompleted[dependentCourse] = True
                        nextNew.add(dependentCourse)
            newCompletedCourses = nextNew
        return len([courseCompleted for courseCompleted in coursesCompleted if courseCompleted]) >= numCourses
 