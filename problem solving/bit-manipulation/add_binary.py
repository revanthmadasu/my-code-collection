'''
    problem: https://leetcode.com/problems/add-binary/
    concepts: bit manipulation, loops
    performance: 39.15% runtime, 55.78% memory
'''
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_len = len(a)
        b_len = len(b)
        n = max(a_len, b_len)
        res = ""
        carry_bit = 0
        for i in range(n):
            a_bit = 0
            b_bit = 0
            if a_len - i - 1 >= 0:
                a_bit = 1 if a[a_len - i - 1] == '1' else 0
            if b_len - i - 1 >= 0:
                b_bit = 1 if b[b_len - i - 1] == '1' else 0
            total = a_bit + b_bit + carry_bit
            if total == 3:
                res = "1" + res
                carry_bit = 1
            elif total == 2:
                res = "0" + res
                carry_bit = 1
            elif total == 1:
                res = "1" + res
                carry_bit = 0
            else:
                res = "0"+ res
                carry_bit = 0
        if carry_bit:
            res = "1" + res
        return res