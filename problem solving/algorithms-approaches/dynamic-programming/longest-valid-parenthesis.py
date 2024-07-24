'''
    Problem: https://leetcode.com/problems/longest-valid-parentheses
    Concepts: Dynamic Programming, Caching
    performance: 18.85% runtime, 6.21% memory
    #todo: implement with tabular DP approach. #revise
'''
'''
(()() ((() ())) )
(()()) ((() ())) )
subproblem: what is the lenght of valid parenthesis starting from ith open parenthesis
'''

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        dpSubprobs = dict()
        def getParenthesisLength(start):
            if start in dpSubprobs:
                return dpSubprobs[start]
            next = start + 1
            while next < len(s) and s[next] == '(':
                subLen = getParenthesisLength(next)
                if subLen == -1:
                    dpSubprobs[start] = -1
                    return -1
                next += subLen
            if next < len(s):
                dpSubprobs[start] = next - start + 1
                if next+1 < len(s) and s[next+1] == '(':
                    nextSubLen = getParenthesisLength(next+1)
                    if nextSubLen != -1:
                        dpSubprobs[start] += nextSubLen
                return dpSubprobs[start]
            else:
                dpSubprobs[start] = -1
                return -1
        maxLen = 0
        for i in range(len(s)):
            if (s[i] == '('):
                maxLen = max(maxLen, getParenthesisLength(i))
        # print(f'{dpSubprobs}')
        return maxLen