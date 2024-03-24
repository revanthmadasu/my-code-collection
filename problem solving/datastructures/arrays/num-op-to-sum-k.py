'''
    problem: https://leetcode.com/contest/weekly-contest-390/problems/apply-operations-to-make-sum-of-array-greater-than-or-equal-to-k/
    concepts: array
    #incomplete - test cases fail
    #todo: complete it
'''
import math
class Solution:
    def minOperations(self, k: int) -> int:
        if k == 1:
            return 0

        minOp = float('inf')
        curVal = 1
        addOpReq = 0
        
        while True:
            numOpp = addOpReq + math.ceil((k-curVal)/curVal)
            if numOpp < minOp:
                minOp = numOpp
                print(curVal)
            else:
                break
            curVal += 1
            addOpReq += 1

        return minOp
