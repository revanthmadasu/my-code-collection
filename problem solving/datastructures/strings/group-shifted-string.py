'''
    problem: https://leetcode.com/problems/group-shifted-strings/
    concepts: String
    performance: 59.97% runtime, 92.99% memory
'''
from typing import List
class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        
        stringsMap = dict()
        for string in strings:
            first = ord(string[0]) - ord('a')
            ords = [ord(ch)-ord('a') for ch in string]
            diffOrds = [_ord-ords[0] for _ord in ords]
            minString = ''.join([chr((_ord if _ord >= 0 else 26+_ord)+ord('a'))for _ord in diffOrds])
            
            # print(f'{string} => {minString}')
            if minString not in stringsMap:
                stringsMap[minString] = []
            stringsMap[minString].append(string)
        return list(stringsMap.values())
