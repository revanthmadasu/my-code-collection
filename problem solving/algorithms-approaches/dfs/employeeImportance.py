'''
    problem: https://leetcode.com/problems/employee-importance/description/
    concepts: trees, dfs
    performance: 69.85% runtime, 51.32% memory
'''

# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

from typing import List
class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        employeesMap = dict()
        for employee in employees:
            employeesMap[employee.id] = employee
        def getImportance(employee):
            _importance = employee.importance
            for sub_ordinate in employee.subordinates:
                _importance += getImportance(employeesMap[sub_ordinate])
            return _importance
        return getImportance(employeesMap[id])