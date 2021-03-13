#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict
# https://www.hackerrank.com/challenges/ctci-making-anagrams/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings
def split(word):
    return [char for char in word] 
def makeAnagram(a, b):
    a_letter_count_map = defaultdict(lambda: None)
    b_letter_count_map = defaultdict(lambda: None)
    for letter in a:
        a_letter_count_map[letter] =(a_letter_count_map[letter] or 0) + 1
    for letter in b:
        b_letter_count_map[letter] =(b_letter_count_map[letter] or 0) + 1
    diff = 0
    for key in a_letter_count_map:
            if key not in b:
                diff += a_letter_count_map[key]
            elif a_letter_count_map[key] > b_letter_count_map[key]:
                # print(f'removing1 .{key}')
                diff += (a_letter_count_map[key] - b_letter_count_map[key])
    for key in b_letter_count_map:
        if key not in a:
            diff += b_letter_count_map[key]
        elif b_letter_count_map[key] > a_letter_count_map[key]:
            # print(f'removing2 .{key}')            
            diff += (b_letter_count_map[key] - a_letter_count_map[key])
    print(''.join(sorted(split(a))))
    print(''.join(sorted(split(b))))
    return diff
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
