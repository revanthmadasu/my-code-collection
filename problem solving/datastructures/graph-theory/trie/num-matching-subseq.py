'''
    problem: https://leetcode.com/problems/number-of-matching-subsequences/
    concepts: Trie, Hashtable
    performance: 5.01% runtime, 5.02% memory
'''
from typing import List
# this straight forward approach is actually best performing - 90.52 runtime, 82.85 memory
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
    
        def is_sub(word):
            index=-1
            for ch in word:
                index=s.find(ch,index+1)
                if index==-1:
                    return False
            return True
        
        c=0
        for word in words:
            if is_sub(word):
                c+=1
        
        return c
#performance: 5.01% runtime, 5.02% memory
# class TrieNode:
#     def __init__(self, val, parent):
#         self.parent = parent
#         self.val = ''
#         self.nextCharNode = dict()
# class Solution:
#     def numMatchingSubseq(self, s: str, words: List[str]) -> int:
#         trieRoot = TrieNode('', None)
#         prevNode = trieRoot
#         for ch in s:
#             node = TrieNode(ch, prevNode)
#             backTrackNode = prevNode
#             while backTrackNode and (ch not in backTrackNode.nextCharNode):
#                 backTrackNode.nextCharNode[ch] = node
#                 backTrackNode = backTrackNode.parent
#             prevNode = node
#         # resWords = []
#         subseqCount = 0
#         for word in words:
#             curNode = trieRoot
#             isSubseq = True
#             for ch in word:
#                 if ch in curNode.nextCharNode:
#                     curNode = curNode.nextCharNode[ch]
#                 else:
#                     isSubseq = False
#                     break
#             subseqCount += int(isSubseq)
#         return subseqCount