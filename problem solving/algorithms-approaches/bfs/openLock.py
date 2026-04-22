'''
    problem: https://leetcode.com/problems/open-the-lock/
    concepts: bfs, hash table, queue
    performance: 92.21% runtime, 13.51% memory
'''
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visitedMap = dict()
        initialComb = (0,0,0,0)
        queue = [initialComb]
        visitedMap[initialComb] = True
        for comb in deadends:
            tComb = tuple([int(ch) for ch in comb])
            if tComb == (0,0,0,0):
                return -1
            visitedMap[tComb] = True
        numMoves = 0
        while len(queue):
            newQueue = []
            for comb in queue:
                strComb = ''.join([str(ch) for ch in comb])
                if strComb == target:
                    return numMoves
                a, b, c, d = comb[0], comb[1], comb[2], comb[3]
                pa, pb, pc, pd = comb[0] + 1, comb[1] + 1, comb[2] + 1, comb[3] + 1
                ma, mb, mc, md = comb[0] - 1, comb[1] - 1, comb[2] - 1, comb[3] - 1
                ma, mb, mc, md = [9 if m == -1 else m for m in [ma, mb, mc, md]]
                pa, pb, pc, pd  = [0 if m == 10 else m for m in [pa, pb, pc, pd]]
                nextCombs = [(pa, b, c, d), (ma, b, c, d), (a, pb, c, d), (a, mb, c, d), (a, b, pc, d), (a, b, mc, d), (a, b, c, pd), (a, b, c, md)]
                nextCombs = [ncomb for ncomb in nextCombs if ncomb not in visitedMap]
                for ncomb in nextCombs:
                    visitedMap[ncomb] = True
                newQueue.extend(nextCombs)
            # print(f'next moves for attempt: {numMoves+1} is {newQueue}')
            queue = newQueue
            numMoves += 1
        return -1