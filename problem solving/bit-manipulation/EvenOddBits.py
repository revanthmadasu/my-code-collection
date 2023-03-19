'''
    https://leetcode.com/contest/weekly-contest-337/problems/number-of-even-and-odd-bits/
    Concepts: bits
'''
class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        binary = bin(n)[2:]
        even = 0
        odd = 0
        b_l = len(binary)
        for i, digit in enumerate(binary):
            ind = b_l-1-i
            if int(digit) == 1:
                if ind%2 == 0:
                    even += 1
                else:
                    odd += 1
        return [even, odd]