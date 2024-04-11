'''
    Problem: https://leetcode.com/problems/add-to-array-form-of-integer/
    Concepts: Array, Math
    performance: 5.04 runtime, 22.29 memory
'''
from typing import List
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        def numFromArray(arr):
            _sum = 0
            for i in range(len(arr)-1, -1, -1):
                _sum += (arr[i] * 10**(len(arr)-1 - i))
            return _sum
        numForm = numFromArray(num)
        numForm = numForm + k
        res = []
        # print(f'{numForm}')
        while numForm:
            res.append(numForm%10)
            numForm = (numForm//10)
        res.reverse()
        return res