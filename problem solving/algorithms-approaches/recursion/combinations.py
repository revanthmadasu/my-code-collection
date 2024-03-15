'''
    https://leetcode.com/problems/combinations/description/
    Concepts: Recursion, Maths, Combinations
    90% runtime, 5 % memory
'''
class Solution:
    def combine(self, n: int, k: int, l = [[]]):
        next_l = []
        ll_len = len(l[0])
        # print(f'll_len is {ll_len}')
        if ll_len == k:
            return l
        for ll in l:
            # print(f'current: ll is {ll}')
            start = 1 if ll_len < 1 else ll[ll_len - 1]+1
            end = n - (k - (ll_len + 1))
            # print(f'start is {start}, end is {end}')
            next_range = range(start, end + 1)
            # print(f'generated range: {next_range}')
            for num in next_range:
                next_l.append(ll + [num])
        return self.combine(n, k, next_l)