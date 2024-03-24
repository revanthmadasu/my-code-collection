'''
    problem: https://leetcode.com/problems/next-closest-time/
    concepts: string
    performance: 38.08% runtime, 92.75% memory
'''
class Solution:
    def nextClosestTime(self, time: str) -> str:
        digits = [*time]
        digits.remove(':')
        # time.replace(':', '')
        combs = set()
        for i in range(len(digits)) :
            for j in range(i, len(digits)):
                combs.add(digits[i]+digits[j])
                combs.add(digits[j]+digits[i])
        combs = list(combs)
        combs.sort()
        hrs, mins = time.split(':')

        minsIndex = combs.index(mins)
        if minsIndex < len(combs)-1:
            if int(combs[minsIndex+1]) < 60:
                return f'{hrs}:{combs[minsIndex+1]}'
        hrsIndex = combs.index(hrs)
        if hrsIndex < len(combs)-1:
            if int(combs[hrsIndex+1]) < 24:
                return f'{combs[hrsIndex+1]}:{combs[0]}'
        return f'{combs[0]}:{combs[0]}'