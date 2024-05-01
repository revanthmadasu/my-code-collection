'''
    Problem: https://leetcode.com/problems/remove-duplicate-letters/
    Concepts: Greedy, String, Subsequence, Stack, Monotonic Stack
    performance: 96.22% runtime, 48.58% memory
'''
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        lastOccurance = {s[i]: i for i in range(len(s))}
        stack = [s[0]]
        visited = set([s[0]])
        for i in range(1, len(s)):
            ch = s[i]
            if ch in visited:
                continue
            while len(stack) and ch < stack[-1] and lastOccurance[stack[-1]] > i:
                prevCh = stack.pop()
                visited.remove(prevCh)
            stack.append(ch)
            visited.add(ch)
        return "".join(stack)