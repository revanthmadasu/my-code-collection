'''
    problem: https://leetcode.com/problems/meeting-scheduler/
    concepts: Intervals, Two Pointers
    performance: 66.47% runtime, 48.24% memory
'''
from typing import List
class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort(key=lambda slot: slot[0])
        slots2.sort(key=lambda slot: slot[0])
        curSlot1 = 0
        curSlot2 = 0
        def doesIntersect(slot1, slot2):
            return not(slot1[0] > slot2[1] or slot2[0] > slot1[1])
        while curSlot1 < len(slots1) and curSlot2 < len(slots2):
            slot1 = slots1[curSlot1]
            slot2 = slots2[curSlot2]
            if slot1[0] > slot2[1]:
                curSlot2 += 1
            elif slot2[0] > slot1[1]:
                curSlot1 += 1
            else:
                start = max(slot1[0], slot2[0])
                end = min(slot1[1], slot2[1])
                if end - start >= duration:
                    return [start, start+duration]
                else:
                    '''
                        (5,20),(34,35)
                        (1,10),(11,70)
                        if current slot from slot1 intersect with next slot from slot2, current slot from slot2 cannot intersect with next slot from slot1, because it is given there is no intersection between any two slots of a person
                    '''
                    if curSlot1+1 < len(slots1) and doesIntersect(slots1[curSlot1+1], slots2[curSlot2]):
                        curSlot1 += 1
                    elif curSlot2+1 < len(slots2) and doesIntersect(slots1[curSlot1], slots2[curSlot2+1]):
                        curSlot2 += 1
                    else:
                        curSlot1 += 1
                        curSlot2 += 1
        return []
