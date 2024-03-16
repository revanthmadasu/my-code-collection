#!/bin/python3

import math
import os
import random
import re
import sys
# https://www.hackerrank.com/challenges/sherlock-and-anagrams/submissions/code/140425640?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps
def sherlockAndAnagrams(s):
    l=len(s)
    total = 0
    for sub_len in range(1,l+1):
        sub_strings = dict()
        for i in range(0,l-sub_len+1):
            sub_string=''.join(sorted(s[i:i+sub_len]))
            if sub_strings.get(sub_string):
                sub_strings[sub_string] += 1
            else:
                sub_strings[sub_string] = 1
        #print(sub_strings)
        for sub_string in sub_strings.keys():
            tmp = sub_strings[sub_string]
            if tmp > 1:
                total += (tmp*(tmp-1))/2
    
    return int(total)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
