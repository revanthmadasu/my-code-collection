from typing import List
'''
    Problem: https://leetcode.com/problems/combination-sum
    Concepts: Recursion, Backtracking
    Performance: 5.83% runtime, 7.09% memory
    #todo: improve performance
'''
class Solution:
    def combinationSum(self, candidates: List[int], target: int, acc = []) -> List[List[int]]:
        sols = self.backtrack(candidates, target)
        unique_sols_str = set()
        for sol in sols:
            str_sol = ''.join(sol)
            unique_sols_str.add(str_sol)
        unique_sols = []
        for str_sol in unique_sols_str:
            unique_sols.append(list(map(int, str_sol.split(''))))
        return unique_sols
    def backtrack(self, candidates: List[int], target: int, acc = []) -> List[List[int]]:
        sols = []
        # print(f'received args: {candidates}, {target}')
        for candidate in candidates:
            if target - candidate == 0:
                comb = acc + [candidate]
                comb.sort()
                comb = list(map(str, comb))
                # print(f'fulfilled comb found {comb}')
                sols.append(comb)
            elif target - candidate > 0:
                sols.extend(self.backtrack(candidates, target - candidate, acc + [candidate]))
        return sols


sol = Solution()

# input 1 ======================>
candidates_1 = [2,3,6,7]
target_1 = 7
print(sol.combinationSum(candidates_1, target_1))