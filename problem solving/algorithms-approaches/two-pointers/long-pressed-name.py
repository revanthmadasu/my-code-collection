'''
    Problem: https://leetcode.com/problems/height-checker
    Concepts: Arrays, sorting
    performance: 26.90% runtime, 24.60% memory
    #todo: improve runtime
'''
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        nameChars = dict()
        p1 = 0
        p2 = 0
        while p1 < len(name) and p2 < len(typed):
            p1Char = name[p1]
            p1Cnt = 0
            while p1 < len(name) and name[p1] == p1Char:
                p1Cnt += 1
                p1 += 1
            p2Char = typed[p2]
            if p1Char != p2Char:
                return False
            p2Cnt = 0
            while p2 < len(typed) and typed[p2] == p2Char:
                p2Cnt += 1
                p2 += 1
            if p2Cnt < p1Cnt:
                return False
        return (p1 == len(name) and p2 == len(typed))