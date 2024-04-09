'''
    Problem: https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string
    Concepts: Stack
    performance: 79.08% runtime, 47.69% memory
'''
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for ch in s:
            if stack and stack[-1] == ch:
                stack.pop()
            else:
                stack.append(ch)
        return ''.join(stack)
            