'''
    problem: https://leetcode.com/problems/strobogrammatic-number
    concepts: string
    performance: 52.58% runtime, 18.62% memory
'''
class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        strobogrammatic = set(["1", "6", "8", "9"])
        strobogrammatic = dict()
        strobogrammatic["0"] = "0"
        strobogrammatic["1"] = "1"
        strobogrammatic["6"] = "9"
        strobogrammatic["8"] = "8"
        strobogrammatic["9"] = "6"
        strobogrammaticNum = ""
        for digit in num:
            if digit not in strobogrammatic:
                return False
            else:
                strobogrammaticNum += strobogrammatic[digit]
        # print(f'strobogrammaticNum: {strobogrammaticNum[::-1]}')
        return int(strobogrammaticNum[::-1]) == int(num)
        