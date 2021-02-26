#!/bin/python3

import math
import os
import random
import re
import sys
# https://www.hackerrank.com/challenges/hackerrank-in-a-string/problem
# Complete the hackerrankInString function below.
def hackerrankInString(s):
    word='hackerrank'
    currentIndex = 0
    for _char in s:
        if _char == word[currentIndex]:
            currentIndex += 1
        if currentIndex == 10:
            break
    return 'YES' if currentIndex == 10 else 'NO'
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)

        fptr.write(result + '\n')

    fptr.close()
