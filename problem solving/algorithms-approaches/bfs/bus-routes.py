'''
    problem: https://leetcode.com/problems/bus-routes/
    concepts: BFS, Hashtable, graphs
    #incomplete - 42/54 testcases passed
    #todo: complete it
'''
from typing import List
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        nextStops = dict()
        sourceBusNos = []
        for busNo, busRoute in enumerate(routes):
            for stationI, station in enumerate(busRoute):
                if station == source:
                    sourceBusNos.append(busNo)
                if station not in nextStops:
                    nextStops[station] = []
                nextStops[station].append((busRoute[(stationI+1)%len(busRoute)], busNo))
        print(nextStops)
        queue = []
        visited = dict()
        for busNo in sourceBusNos:
            queue.append((source, busNo))
            visited[(source, busNo)] = 1
        while len(queue):
            newQueue = []
            for stationBus in queue:
                if target in routes[stationBus[1]]:
                    return visited[(stationBus[0], stationBus[1])]
                nextStationBusses = [nextStationBus for nextStationBus in nextStops[stationBus[0]] if nextStationBus not in visited]

                for nextStationBus in nextStationBusses:
                    visited[(nextStationBus[0], nextStationBus[1])] = visited[(stationBus[0], stationBus[1])] +  int(stationBus[1] != nextStationBus[1])
                newQueue.extend(nextStationBusses)
            queue = newQueue
        return -1

