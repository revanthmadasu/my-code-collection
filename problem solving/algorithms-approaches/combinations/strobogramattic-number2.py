'''
    problem: https://leetcode.com/problems/strobogrammatic-number-ii/
    concepts: string, combinations
    performance: 65.47% runtime, 34.72% memory
'''
from typing import List
class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        base1 = ["0", "1","8"]
        base2 = ["11","69","88","96"]
        if n == 0:
            return []
        elif n == 1:
            return ["0","1","8"]
        elif n == 2:
            return base2
        
        r, res = (n-1, base1) if n%2 == 1 else (n-2, ["11","69","88","96", "00"])
        # base1.remove("0")
        for i in range(r//2):
            # print(f'{i}th time')
            newRes = []
            for sub in res:
                for ch in ["1", "8", "0"]:
                    if i == (r//2)-1:
                        if ch == "0":
                            continue
                    newRes.append(f'{ch}{sub}{ch}')
                newRes.append(f'6{sub}9')
                newRes.append(f'9{sub}6')
            res = newRes
        # res.remove("0"*n)
        return list(set(res))
