#!/bin/python
# https://www.hackerrank.com/challenges/strange-advertising/problem
import math
import os
import random
import re
import sys

def viralAdvertising(n):
    liked = []
    cur_shared = 5
    cumulative = 0
    cur_liked = 0
    for i in range(1, n+1):
        cur_liked = math.floor(cur_shared/2)
        cumulative += cur_liked
        cur_shared = cur_liked*3
    return int(cumulative)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
