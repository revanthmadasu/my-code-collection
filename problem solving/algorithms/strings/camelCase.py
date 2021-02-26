#!/bin/python3

import math
import os
import random
import re
import sys

# https://www.hackerrank.com/challenges/camelcase/problem
def isLetterCapital(letter):
    asci = ord(letter)
    return asci >= 65 and asci <= 90
def camelcase(s):
    total = 0
    for _char in s:
        if isLetterCapital(_char):
            total+=1
    return total + 1
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = camelcase(s)

    fptr.write(str(result) + '\n')

    fptr.close()
