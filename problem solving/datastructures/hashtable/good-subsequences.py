'''
    problem: https://leetcode.com/problems/count-the-number-of-good-subsequences
    concepts: Hash Table, Counting, Combinatorics
    performance: 29.17% runtime, 60.42% memory
'''
class Solution:
    def countGoodSubsequences(self, s: str) -> int:
        counts = dict()
        @lru_cache
        def nCr(n,r):
            return math.comb(n,r)
            # return math.factorial(n)//(math.factorial(n-r) * math.factorial(r))
        count = 0
        ct = Counter(s)
        _max = max(ct.values())
        for freq in range(1, _max+1):
            combC = 1
            for ch in ct:
                if ct[ch] >= freq:
                    combC *= (nCr(ct[ch], freq)+1)
            count += (combC-1)
        # for i in range(len(s)):
        #     ch = s[i]
        #     if ch not in counts:
        #         counts[ch] = 0
        #     counts[ch] += 1
        #     for freq in range(1, counts[ch]+1):
        #         numWays = [nCr(counts[c], freq)+1 for c in counts if counts[c] >= freq and c != ch]
        #         numWays.append(nCr(counts[ch]-1, freq-1))
        #         count += functools.reduce(lambda x,y: x*y, numWays)
        return count % 1000000007
