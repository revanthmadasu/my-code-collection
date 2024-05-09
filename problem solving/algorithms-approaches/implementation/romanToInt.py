'''
    problem: https://leetcode.com/problems/roman-to-integer
    concepts: strings, hashtable/hashmap
    performance: 96.36% runtime, 92.44% memory
'''
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        mapped = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        i = 0
        n = len(s)
        num = 0
        while i < n:
            if i-1 >= 0 and mapped[s[i-1]] < mapped[s[i]]:
                num = num - 2*mapped[s[i-1]] + mapped[s[i]]
            else:
                num += mapped[s[i]]
            i+=1
        return num
    
# asked in oracle interview - same solutions provided
class Solution:
    def romanToInt(self, s: str) -> int:
        romanStr = s
        valuesMap = {'I': 1, 'V': 5, 'X':10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res = valuesMap[romanStr[0]]
        for i in range(1, len(romanStr)):
            sym = romanStr[i]
            prevSym = romanStr[i-1]
            if valuesMap[sym] > valuesMap[prevSym]:
                res -= (2 * valuesMap[prevSym])
            res += valuesMap[sym]
        return res