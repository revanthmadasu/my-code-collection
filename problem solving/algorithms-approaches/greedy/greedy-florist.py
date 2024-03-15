#!/bin/python3

import math
import os
import random
import re
import sys

#https://www.hackerrank.com/challenges/greedy-florist/problem
def getMinimumCost(k, c):
    n = len(c)
    total = 0
    c.sort(reverse=True)
    multiplier = 0
    for i in range(0,n,k):
        multiplier += 1
        total += (sum(c[i:i+k])*multiplier)
    return total
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)

    fptr.write(str(minimumCost) + '\n')

    fptr.close()
