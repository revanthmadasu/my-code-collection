#!/bin/python3

import math
import os
import random
import re
import sys

# https://www.hackerrank.com/challenges/mars-exploration/problem
def marsExploration(s):
    uncorrect = 0
    for i in range(len(s)):
        curLetter = s[i]
        expected = 'S' if (i%3 == 2 or i%3 == 0) else 'O'
        if not curLetter == expected:
            uncorrect += 1
    return uncorrect
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
