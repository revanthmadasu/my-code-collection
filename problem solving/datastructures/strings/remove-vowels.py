'''
    problem: https://leetcode.com/problems/remove-vowels-from-a-string
    concepts: String
    performance: 93.75% runtime, 13.43% memory
'''
class Solution:
    def removeVowels(self, s: str) -> str:
        withoutVowels = ""
        for ch in s:
            if ch not in ['a','e','i','o','u']:
                withoutVowels += ch
        return withoutVowels  