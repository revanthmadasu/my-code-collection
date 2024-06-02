'''
    problem: https://leetcode.com/problems/minimum-one-bit-operations-to-make-integers-zero/
    concepts: Dynamic Programming, Bit Manipulation
    performance: 6.43% runtime, 8.93% memory
    #todo: improve performance, reduce redundant calls
'''
import math
class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        @cache
        def changeToZero(num):
            # print(f'zero call: {num}, from: {_from}')
            if num == 0:
                return 0
            elif num == 1:
                return 1
            pow = math.floor(math.log(num, 2))
            isNextBitOne = num - 2**pow >= 2**(pow-1)
            if isNextBitOne:
                numways = changeToZero(num - 2**pow - 2**(pow-1))
            else:
                numways = changeToOne(num - 2**pow, pow-1)
            numways += 1
            # print(f'changed from {num} to {2**(pow-1)} in {numways}')
            zways = changeToZero(2**(pow-1))
            # print(f'ret 0 call: changed from {2**(pow-1)} to {0} in {zways}')
            numways += zways
            return numways
        @cache
        def changeToOne(num, pow):
            # print(f'one call: {num}, from: {_from}, pow: {pow}')
            target = 2**(pow)
            numways = 0
            orNum = num
            # print(f'target is {target}')
            while num != target:
                if num == 0:
                    num = 1
                    numways += 1
                    continue
                elif num == 1:
                    num = 2
                    numways += 2
                    continue
                pow = math.floor(math.log(num, 2))
                numways += (changeToZero(num - 2**pow) + 1)
                numways += changeToZero(2**pow)
                num = 2**(pow+1)
                # print(f'changed to {num}')
            # print(f'ret 1 call: changed from {orNum} to {num} in {numways}')
            return numways
        return changeToZero(n)