'''
    problem: https://leetcode.com/problems/asteroid-collision
    concepts: stack
    performance: 92.52% runtime, 9.85% memory
'''
from typing import List
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        resDict = dict()
        for i in range(len(asteroids)):
            asteroid = asteroids[i]
            if asteroid > 0:
                resDict[i] = True
                stack.append((asteroid, i))
            else:
                while stack and stack[-1][0] < abs(asteroid):
                    posAstr, posIndex = stack.pop()
                    resDict[posIndex] = False
                if stack:
                    if stack[-1][0] == abs(asteroid):
                        posAstr, posIndex = stack.pop()
                        resDict[i] = False
                        resDict[posIndex] = False
                    else:
                        resDict[i] = False
                else:
                    resDict[i] = True
        res = []
        for i in range(len(asteroids)):
            if resDict[i]:
                res.append(asteroids[i])
        return res