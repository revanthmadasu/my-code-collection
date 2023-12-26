'''
    problem: https://leetcode.com/problems/minimum-genetic-mutation
    concepts: bfs
    performance: 96.02% runtime, 5.29% memory
    #todo: improve memory - try removing visited dictionary
'''
from typing import List
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        n = len(startGene)
        if n == len(endGene) and endGene in bank:
            if startGene == endGene:
                return 0
            visited = {}
            visited[startGene] = True
            queue = [startGene]
            result = False
            count = 0
            while len(queue):
                new_queue = []
                count += 1
                for queue_item in queue:
                    if result:
                        break
                    visited[queue_item] = True
                    for i in range(n):
                        if result:
                            break
                        for new_ch in ['A', 'C', 'G', 'T']:
                            new_mutation = queue_item[:i] + new_ch + queue_item[i+1:]
                            if (visited.get(new_mutation) == None) and new_mutation in bank:
                                if new_mutation == endGene:
                                    result = True
                                    queue = []
                                    new_queue = []
                                    break
                                else:    
                                    new_queue.append(new_mutation)
                queue = new_queue
            if result:
                return count
            else:
                return -1 
        else:
            return -1
        
sol = Solution()

input1 = ["AACCGGTT", "AACCGCTA", ["AACCGGTA","AACCGCTA","AAACGGTA"]]
# "AACCGGTT" -> "AACCGGTA" -> "AACCGCTA"

print(sol.minMutation(input1[0], input1[1], input1[2]))