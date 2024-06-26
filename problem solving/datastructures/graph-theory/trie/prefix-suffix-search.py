'''
    Problem: https://leetcode.com/problems/prefix-and-suffix-search/
    Concepts: Trie, BFS
    #incomplete: 16/17 testcases passed. Time limit exceeded
    #todo: complete it - try with dfs
'''
from collections import deque
from typing import List
class WordFilter:

    def __init__(self, words: List[str]):
            
        self.trie = dict()
        def addWord(word, i):
            node = self.trie
            for ch in word:
                if ch not in node:
                    node[ch] = dict()
                    node[ch]['wordIndex'] = -1
                node = node[ch]
            node['wordIndex'] = i
            
        for i, word in enumerate(words):
            addWord(word, i)
    def f(self, pref: str, suff: str) -> int:
        node = self.trie
        for ch in pref:
            if ch in node:
                node = node[ch]
            else:
                return -1
        sufLen = len(suff)
        qNodes = deque()
        qNodes.append((node, pref[-sufLen:]))
        maxIndex = -1
        if pref[-sufLen:] == suff:
            maxIndex = node['wordIndex']
        while len(qNodes):
            node, sufWord = qNodes.popleft()
            # print(f'extracted word: {sufWord}')
            if sufWord == suff:
                maxIndex = max(maxIndex, node['wordIndex'])
            nextChars = list(filter(lambda k: k != 'wordIndex', node))
            nextCharNodes = list(map(lambda ch: node[ch], nextChars))
            for i in range(len(nextChars)):
                qNodes.append((nextCharNodes[i], (sufWord+nextChars[i])[-sufLen:]))
        return maxIndex

'''
    sets approach - 
    performance: 95.77% runtime, 80.69% memory
'''
from collections import defaultdict

class WordFilter:

    def __init__(self, words: List[str]):
        self.prefixes = defaultdict(set)
        self.suffixes = defaultdict(set)
        seen = set()
        for idx in range(len(words) - 1, -1, -1):
            word = words[idx]
            if word in seen:
                continue
            seen.add(word)
            for i in range(0, len(word) + 1):
                prefix = word[:i]
                suffix = word[i:]
                self.prefixes[prefix].add(idx)
                self.suffixes[suffix].add(idx)

    def f(self, pref: str, suff: str) -> int:
        if pref in self.prefixes and suff in self.suffixes:
            sharedWords = self.prefixes[pref] & self.suffixes[suff]
            return max(sharedWords) if sharedWords else -1
        return -1


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)