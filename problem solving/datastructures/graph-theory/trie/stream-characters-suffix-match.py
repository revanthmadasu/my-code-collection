'''
    Problem: https://leetcode.com/problems/stream-of-characters/
    Concepts: Trie, Stream
    performance: 46.57% runtime, 5.07% memory
'''
from typing import List
class TrieNode:
    def __init__(self, val, parent):
        self.val = val
        self.childMap = dict()
        self.parent = parent
        self.fullWord = False
        if parent:
            parent.childMap[val] = self

class StreamChecker:

    def __init__(self, words: List[str]):
        self.trieRoot = TrieNode('', None)
        self.queryString = ''
        def addWordToTrie(word):
            curTrieNode = self.trieRoot
            for ch in word:
                if ch in curTrieNode.childMap:
                    curTrieNode = curTrieNode.childMap[ch]
                else:
                    curTrieNode = TrieNode(ch, curTrieNode)
            curTrieNode.fullWord = True
        for word in words:
            addWordToTrie(word[::-1])


    def query(self, letter: str) -> bool:
        self.queryString = letter + self.queryString
        curTrieNode = self.trieRoot
        # print(f'query string: {self.queryString}')
        for ch in self.queryString:
            if ch in curTrieNode.childMap:
                # print(f'{ch} exists in {curTrieNode.val}')
                curTrieNode = curTrieNode.childMap[ch]
                # print(f'{ch} is fullword ? {curTrieNode.fullWord}')
                if curTrieNode.fullWord:
                    return True
            else:
                return False
        return curTrieNode.fullWord


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)