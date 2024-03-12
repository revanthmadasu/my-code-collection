'''
    problem: https://leetcode.com/problems/powx-n
    concepts: math, recursion
    performance: 97.49% runtime, 32.99% memory
'''
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 1 or x == 0:
            return x
        if x == -1:
            return -1 if n%2 == 1 else 1
        if n == 0:
            return 1
        if n < 0:
            n = -n
            x = 1/x

        def getPowRecursively(n1, x):
            if n1 == 1:
                return x
            prod = getPowRecursively(n1//2, x)
            return prod * prod * (x if n1%2 == 1 else 1)
        
        power = getPowRecursively(n, x)
        return power
