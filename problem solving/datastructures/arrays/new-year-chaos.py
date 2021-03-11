#!/bin/python3

import math
import os
import random
import re
import sys

# https://www.hackerrank.com/challenges/new-year-chaos/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
def minimumBribes(q):
    ary = []
    flag = False
    bribeCount = 0
    for i in range(len(q)-1, -1, -1):
        index = i+1
        diff = q[i] - index
        if diff > 2:
            flag = True
            break
        else:
            for j in range(max(0,q[i] - 2), i):
                if q[j] > q[i]:
                    bribeCount += 1
    if (flag):
        print('Too chaotic')
    else:
        print(bribeCount)
if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
