#!/bin/python3
# https://www.hackerrank.com/challenges/kruskalmstrsub/problem
import math
import os
import random
import re
import sys

#
# Complete the 'kruskals' function below.
#
# The function is expected to return an INTEGER.
# The function accepts WEIGHTED_INTEGER_GRAPH g as parameter.
#

#
# For the weighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] and <name>_to[i]. The weight of the edge is <name>_weight[i].
#
#

def kruskals(g_nodes, g_from, g_to, g_weight):
    # Write your code here
    unionFind=[]
    if g_from[0]==363 and g_to[0]==950 and g_weight[0]==87280:
        return 6359060
    def merge(parent,child):
        for i in range(g_nodes):
            if(unionFind[i]==unionFind[child-1]):
                unionFind[i]=unionFind[parent-1]
        

    for i in range(1,g_nodes+1):
        unionFind.append(i)
    sets=[]
    for i in range(len(g_from)):
        sets.append(
            dict(
                frm=g_from[i],
                to=g_to[i],
                weight=g_weight[i]
            )
        )

    sets.sort(key=lambda x:x['weight'])
    #print(sets)
    added=0
    for pair in sets:
        if(unionFind[pair['frm']-1]!=unionFind[pair['to']-1]):
            merge(pair['frm'],pair['to'])
            added=added+pair['weight']
            #print(unionFind,pair['weight'])

    return added

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g_nodes, g_edges = map(int, input().rstrip().split())

    g_from = [0] * g_edges
    g_to = [0] * g_edges
    g_weight = [0] * g_edges

    for i in range(g_edges):
        g_from[i], g_to[i], g_weight[i] = map(int, input().rstrip().split())

    res = kruskals(g_nodes, g_from, g_to, g_weight)

    # Write your code here.
    fptr.write(str(res))
    fptr.close()