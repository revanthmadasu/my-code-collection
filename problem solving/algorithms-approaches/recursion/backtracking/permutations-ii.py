'''
    Problem: https://leetcode.com/problems/permutations-ii
    Concepts: Backtracking, Recursion, Sets
    performance: 14.34% runtime, 5.05% memory
    #todo: improve performance
'''
from typing import List
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(perms, n, cur):
            nextPerms = []
            for perm in perms:
                for i in range(n):
                    if i not in perm:
                        nextPerms.append(perm + [i])
            if cur+1 < n:
                return backtrack(nextPerms, n, cur+1)
            else:
                return nextPerms
        permIs = backtrack([[]], len(nums), 0)
        # print(f'{permIs}')
        perms = set()
        for permI in permIs:
            perms.add(tuple(map(lambda i: nums[i],permI)))
        return perms