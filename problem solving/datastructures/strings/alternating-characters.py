#!/bin/python3

import math
import os
import random
import re
import sys
# https://www.hackerrank.com/challenges/alternating-characters/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings
def alternatingCharacters(s):
    prev = ''
    total = 0
    for letter in s:
        if letter == prev:
            total += 1
        prev = letter
    return total
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()
