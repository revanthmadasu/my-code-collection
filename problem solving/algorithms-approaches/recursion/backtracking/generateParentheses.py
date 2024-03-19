
'''
    problem: https://leetcode.com/problems/generate-parentheses/
    concepts: recursion, backtracking
    performance: 41.86% runtime, 5.78% memory
'''
from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        cache = dict()
        cache[1] = ["()"]
        def myJoin(arr1, arr2):
            res = []
            for s1 in arr1:
                for s2 in arr2:
                    res.append(s1+s2)
            return res
        def recursivelyGenerate(num):
            if num in cache:
                return cache[num]
            else:
                prevRes = recursivelyGenerate(num-1)
                res = []
                for prevParen in prevRes:
                    res.append(f'({prevParen})')
                    res.append(f'{prevParen}()')
                    res.append(f'(){prevParen}')
                for i in range(2, num-1):
                    res.extend(myJoin(recursivelyGenerate(i), recursivelyGenerate(num-i)))

                res = list(set(res))
                cache[num] = res
                return sorted(res)
  

        # print(j(n))
        res = recursivelyGenerate(n)
        print(cache)
        return res