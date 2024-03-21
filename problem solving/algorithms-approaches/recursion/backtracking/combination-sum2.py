'''
    problem: https://leetcode.com/problems/combination-sum-ii
    concepts: recursion, backtracking, combinations
    performance: 5.03% runtime, 11.41% memory
    #todo: improve performance
'''
from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        numsCount = dict()
        for candidate in candidates:
            if candidate not in numsCount:
                numsCount[candidate] = 0
            numsCount[candidate] += 1
        def dfs(_sum, choices, acc):
            if len(choices) == 0:
                return set()
            # res1 = set()
            res = set()
            for i in range(numsCount[choices[0]]+1):
                numSelections = (choices[0],) * i
                print(numSelections)
                if _sum + choices[0]*i < target:
                    res = res.union(dfs(_sum + choices[0]*i, choices[1:], acc+numSelections))
                elif _sum + choices[0]*i == target:
                    res.add(acc+((choices[0],) * i))
            return res

        candidates.sort()
        combs = dfs(0, list(set(candidates)), tuple())
        res = [list(comb) for comb in combs]
        return res

            