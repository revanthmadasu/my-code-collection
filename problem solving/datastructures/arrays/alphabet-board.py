'''
    problem: https://leetcode.com/problems/alphabet-board-path
    concepts: Matrix, Array Traversal
    performance: 51.16% runtime, 60.93% memory
'''
class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        '''
        a - 0
        l - 11
        11%5 = 1
        11//5 = 2
        zdz - "DDDDD!UUUUURRR!DDDDLLLD!"
        '''
        res = ""
        curPos = (0, 0)
        for ch in target:
            i = ord(ch) - ord('a')
            r = i // 5
            c = i % 5
            rDiff = abs(curPos[0] - r)
            cDiff = abs(curPos[1] - c)
            if r < curPos[0]:
                res += ('U'*rDiff)
            if c < curPos[1]:
                res += ('L'*cDiff)
            if c > curPos[1]:
                res += ('R'*cDiff)
            if r > curPos[0]:
                res += ('D'*rDiff)

            res += '!'
            curPos = (r, c)
        return res