'''
    problem: https://leetcode.com/problems/reverse-bits
    concepts: binary
    performance: 48.44% runtime, 51.42% memory
'''
class Solution:
    def reverseBits(self, n: int) -> int:
        bin_n = str(bin(n))[2:]
        _len = len(bin_n)
        if _len < 32:
            bin_n = '0' * (32-_len) + bin_n
        rev_bin = bin_n[::-1]
        return int(rev_bin, 2)
        