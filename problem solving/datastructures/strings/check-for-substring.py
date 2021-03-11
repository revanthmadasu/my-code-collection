#!/bin/python3
# https://www.hackerrank.com/challenges/two-strings/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps
import math
import os
import random
import re
import sys
from collections import defaultdict
def twoStrings(s1, s2):
    flag = False
    checked = defaultdict(lambda: None)
    for letter1 in s1:
        if not checked[letter1]:
            for letter2 in s2:
                if letter1 == letter2:
                    flag = True
                    break
            checked[letter1] = True
        if flag:
            break
    return ((not flag) and "NO") or "YES"
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
