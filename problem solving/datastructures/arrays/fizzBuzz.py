'''
    Problem: https://leetcode.com/problems/fizz-buzz
    Concepts: Loops
    performance: 88.32% runtime, 82.39% memory
'''
from typing import List
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        n1 = n
        res = []
        for i in range(n1):
            n = i+1
            if n%3 == 0 and n%5 == 0:
                res.append("FizzBuzz")
            elif n%3 == 0:
                res.append("Fizz")
            elif n%5 == 0:
                res.append("Buzz")
            else:
                res.append(str(n))
        return res