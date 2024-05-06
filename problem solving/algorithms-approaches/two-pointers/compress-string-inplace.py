'''
    Problem: https://leetcode.com/problems/string-compression/
    Concepts: Two Pointers, String
    performance: 93.67% runtime, 30.34% memory
'''
from typing import List
class Solution:
    def compress(self, chars: List[str]) -> int:
        p1 = p2 = 0
        while p2 < len(chars):
            ch = chars[p2]
            start = p2
            while p2 < len(chars) and chars[p2] == ch:
                p2 += 1
            charCount = p2 - start
            # print(f'p1 is {p1}, chars: {chars}, ch: {ch}, count: {charCount}, p2: {p2}, start: {start}')
            chars[p1] = ch
            p1 += 1
            if charCount > 1:
                countChars = list(str(charCount))
                for countChar in countChars:
                    chars[p1] = countChar
                    p1 += 1
        return p1
            
