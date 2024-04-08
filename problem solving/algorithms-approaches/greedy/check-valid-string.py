'''
    problem: https://leetcode.com/problems/valid-parenthesis-string
    concepts: Greedy
    performance: 78.84% runtime, 21.40% memory
'''
class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMin = 0
        leftMax = 0
        for ch in s:
            if ch == '(':
                  leftMin += 1
                  leftMax += 1
            elif ch == '*':
                leftMin = max(0, leftMin-1)
                leftMax += 1
            else:
                leftMin = max(0, leftMin-1)    
                leftMax -= 1
                if leftMax < 0:
                    return False
        return leftMin == 0