'''
    problem: https://leetcode.com/problems/text-justification
    concepts: sliding window, string, hash table
    performance: 28.33% runtime, 53.70% memory
    #todo: improve performance
'''
from typing import List
class Solution:
    '''
        Straight forward logic. From starting of string, take window. In that window, as the words are of same length, divide equally and check its count using hash table
    '''
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        num_words = len(words)
        word_len = len(words[0])
        window_len = num_words * word_len
        string_len = len(s)
        res = []
        words_map = dict()
        for word in words:
            if not word in words_map:
                words_map[word] = 0
            words_map[word] +=1
        # print(f'num words: {num_words}')

        for i in range(0, string_len - window_len + 1):
            cur_words_map = dict()
            cur_word = s[i:i+window_len]
            # print(f'cur word: {cur_word}')
            for word in words:
                cur_words_map[word] = 0
            possible = True
            for next_word_index in range(num_words):
                # print(f'next_word_i: {next_word_index}')
                start_index = next_word_index * word_len
                next_word = cur_word[start_index:start_index + word_len]
                # print(f'checking word: {next_word}, start: {start_index}, end:{start_index + word_len}')
                if next_word in words:
                    # print(f'matched {next_word}')
                    cur_words_map[next_word] += 1
                else:
                    possible = False
                    break
            # print('printing map')
            # for word in words:
                # print(f'{word}: {words_map[word]}')
            possible = possible and all([words_map[word] == cur_words_map[word] for word in words])
            if possible:
                res.append(i)
        return res


sol = Solution()
print(sol.findSubstring("barfoothefoobarman", ["foo","bar"]))
