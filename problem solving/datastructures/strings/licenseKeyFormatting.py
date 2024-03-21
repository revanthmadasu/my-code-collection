'''
    problem: https://leetcode.com/problems/license-key-formatting
    concepts: string
    performance: 90.95% runtime, 45.08% memory
'''
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        reformatted = s.replace('-', '').upper()
        n = len(reformatted)
        res = []
        while n > 0:
            if n-k-1 >= 0:
                res.append(reformatted[n-k:n])
            else:
                res.append(reformatted[0:n])
            n -= k
        res.reverse()
        return '-'.join(res)