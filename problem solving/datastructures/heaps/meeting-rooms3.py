'''
    Problem: https://leetcode.com/problems/meeting-rooms-iii/
    Concepts: Heap, Sorting
    performance: 92.24% runtime, 50.41% memory
'''
from typing import List
import heapq
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings = sorted(meetings, key=lambda meeting: meeting[0])
        occupanyCounts = [0] * n
        currentlyOccupied = [] # (endTimestamp, index)
        freeRooms = [i for i in range(n)]
        heapq.heapify(currentlyOccupied)
        heapq.heapify(freeRooms)
        curMaxRoomI = 0
        for i in range(len(meetings)):
            # print(f'meeting - {i}')
            # print(f'free rooms: {freeRooms}')
            # print(f'occupied rooms: {currentlyOccupied}')
            meeting = meetings[i]
            while currentlyOccupied and currentlyOccupied[0][0] <= meeting[0]:
                endTime, roomIndex = heapq.heappop(currentlyOccupied)
                heapq.heappush(freeRooms, roomIndex)
            meetingRoom = None
            # print(f'free rooms: {freeRooms}')
            # print(f'occupied rooms: {currentlyOccupied}')
            if freeRooms:
                meetingRoom = heapq.heappop(freeRooms)
                heapq.heappush(currentlyOccupied, (meeting[1], meetingRoom))
            else:
                endTime, meetingRoom = heapq.heappop(currentlyOccupied)
                newEndtime = meeting[1] - meeting[0] + endTime
                heapq.heappush(currentlyOccupied, (newEndtime, meetingRoom))
            occupanyCounts[meetingRoom] += 1
            if occupanyCounts[meetingRoom] > occupanyCounts[curMaxRoomI] or (occupanyCounts[meetingRoom] == occupanyCounts[curMaxRoomI] and meetingRoom < curMaxRoomI):
                curMaxRoomI = meetingRoom
        # print(f'occupancy counts: {occupanyCounts}')
        return curMaxRoomI
