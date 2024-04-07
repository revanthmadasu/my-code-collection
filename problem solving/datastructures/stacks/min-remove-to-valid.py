'''
    problem: https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
    concepts: stack
    performance: 98.21 runtime, 95.51 memory
'''
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        remove = []
        for i in range(len(s)):
            sym = s[i]
            if sym == '(':
                stack.append(i)
            elif sym == ')':
                if len(stack):
                    stack.pop()
                else:
                    remove.append(i)
        while len(stack):
            remove.append(stack.pop())
        remove.sort()
        # print(f'remove indices: {remove}')
        cur = 0
        intervals = []
        for i in remove:
            intervals.append((cur, i))
            cur = i+1
        intervals.append((cur, len(s)))
        # print(f'intervals: {intervals}')
        resString = ''
        for interval in intervals:
            resString += s[interval[0]:interval[1]]
        
        return resString
