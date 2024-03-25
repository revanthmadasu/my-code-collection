'''
    problem: https://leetcode.com/problems/unique-word-abbreviation/
    concepts: Hashtable
    performance: 75.72 runtime, 98.55 memory
'''
from typing import List
class ValidWordAbbr:
    def __init__(self, dictionary: List[str]):
        self.abbrsDict = dict()
        for word in dictionary:
            abbr = self.getAbbr(word)
            if abbr in self.abbrsDict and word != self.abbrsDict[abbr]:
                self.abbrsDict[abbr] = False
            else:
                self.abbrsDict[abbr] = word
    def getAbbr(self, word):
        if len(word) <= 2:
            return word
        return word[0] + str(len(word[1:-1])) + word[-1]
    def isUnique(self, word: str) -> bool:
        abbr = self.getAbbr(word)
        if abbr not in self.abbrsDict:
            return True
        else:
            return self.abbrsDict[abbr] == word


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)