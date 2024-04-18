'''
    Problem: https://leetcode.com/problems/length-of-the-longest-valid-substring/
    Concepts: Sliding Window, Two Pointers
    performance: 21.15% runtime, 58.25% memory
'''
from typing import List
class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        forbidden = set(forbidden)
        left = None
        maxLen = 0
        if len(word) == 1 and word in forbidden:
            return 0
        for i in range(len(word)):
            for j in range(10):
                curLeft = i-j
                if curLeft < 0 or curLeft == left:
                    break
                # print(f'curleft is {curLeft}')
                s = word[curLeft:i+1]
                # print(f's is {s}')
                if s in forbidden:
                    # print(f'forbidden')
                    left = curLeft
                    # print(f'left bound updated to : {left}')
                    break
            # print(f'{word[left+1 if left != None else 0:i+1]} satisfies - left: {left}, len: {len(word[left+1 if left != None else 0:i+1])}')
            maxLen = max(maxLen, len(word[left+1 if left != None else 0:i+1]))
        # sliding window checks in complete boundary - time limit exceeds - not needed as the forbidden strings are of size 10, we only need to check upto 10 characters.
        # while right < len(word):
        #     s = word[left:right+1]
        #     # print(f'{s}')
        #     containsForbidden = False
        #     for forbiddenString in forbidden:
        #         if forbiddenString in s:
        #             left += 1
        #             containsForbidden = True
        #             break
        #     if not containsForbidden:
        #         right += 1
        #     if left > right:
        #         right = left
        #     maxLen = max(maxLen, right-left)
        return maxLen
