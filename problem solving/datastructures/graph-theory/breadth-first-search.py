#!/bin/python3
# https://www.hackerrank.com/challenges/bfsshortreach/problem
import math
import os
import random
import re
import sys

# Complete the bfs function below.
def bfs(n, m, edges, s):
    graph = dict()
    for i in range(1,n+1):
        graph[i]=dict()
        graph[i]['reachability']=-1
        graph[i]['list']=[]
        graph[i]['visited']=False
    for (u,v) in edges:
        if u in graph:
            graph[u]['list'].append(v)
        if v in graph:
            graph[v]['list'].append(u)
    queue=list(graph[s]['list'])
    graph[s]['reachability']=0
    graph[s]['visited']=True
    for vertex in graph[s]['list']:
        graph[vertex]['reachability']=1
        graph[vertex]['visited']=True
    current_reachability=1
    for vertex in queue:
        for next_vertex in graph[vertex]['list']:
            if not graph[next_vertex]['visited']:
                graph[next_vertex]['reachability']=graph[vertex]['reachability']+1
                graph[next_vertex]['visited']=True
                queue.append(next_vertex)
    result=[]
    for i in range(1,n+1):
        if i!=s:
            result.append(graph[i]['reachability']*6 if graph[i]['reachability']!=-1 else -1 )
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input())

        result = bfs(n, m, edges, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()