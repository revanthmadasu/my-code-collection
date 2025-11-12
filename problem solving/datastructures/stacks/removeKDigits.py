'''
    Problem: https://leetcode.com/problems/remove-k-digits
    Concepts: Stack
    performance: 6.85% runtime, 5.38% memory
'''
from collections import deque
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = deque()
        for i in range(len(num)):
            digit = int(num[i])
            while len(stack) > 0 and stack[len(stack)-1] > digit and k > 0:
                k -= 1
                stack.pop()
            stack.append(digit)
        while k > 0:
            stack.pop()
            k -= 1
        while len(stack) > 0 and stack[0] == 0:
            stack.popleft()
        return "0" if len(stack) == 0 else "".join([str(d) for d in stack])
