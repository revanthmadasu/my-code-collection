'''
    problem: https://leetcode.com/problems/text-justification
    concepts: arrays, strings
    performance: 29.21% runtime, 70.29% memory
'''
from typing import List
import math
class Solution:
    '''
        approach:
        greedy approach. try to fill the line with max possible words with space in between.
        then after everything is fit, check if we have any remaining available positions.
        for the spaces in between words add those spaces. Since extra spaces should be positioned at left, use ceil function to get highest possible spaces on left.
    '''
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        cur_word_i = 0
        n = len(words)
        # each iteration in loop gives a new line
        while cur_word_i < n:
            # initially, for every new line, it has max capacity
            available_spaces = maxWidth
            i = cur_word_i
            next_words_count = 0
            while i < n and available_spaces - (len(words[i]) + int(available_spaces != maxWidth)) >= 0:
                next_words_count += 1
                # from the available capacity, remove cur word size and a space if its not first word
                available_spaces -= (len(words[i]) + int(available_spaces != maxWidth))
                i += 1
            # space_count represents spaces after each word. default space is 1 and no space after last word
            space_count = [int(i!= next_words_count-1) for i in range(next_words_count)]
            if i >= n: # last line
                res.append(' '.join(words[cur_word_i:n]) + ' '*available_spaces)
                break
            if next_words_count == 1:
                space_count[0] = available_spaces
            else:
                for i in range(next_words_count-1):
                    adjust_space = math.ceil(available_spaces/(next_words_count-1-i))
                    space_count[i] += adjust_space
                    available_spaces -= adjust_space
            res_str = ""
            for i in range(cur_word_i, cur_word_i+next_words_count):
                res_str += (words[i] + ' '*space_count[i-cur_word_i])
            res.append(res_str)
            cur_word_i += next_words_count
        return res
sol = Solution()
# print(sol.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16))
print(sol.fullJustify(["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], 20))