'''
    problem: https://leetcode.com/problems/finding-the-number-of-visible-mountains
    concepts: monotonic stack, array, sorting
    performance: 43.50% runtime, 93.22% memory
'''
from typing import List
class Solution:
    def visibleMountains(self, peaks: List[List[int]]) -> int:
        monotonic_stack = [float('inf')]
        rightToLeft = set()
        peaks.sort()

        for i in range(len(peaks)-1, -1, -1):
            peak = peaks[i]
            x_inter = peak[0] - peak[1]
            if tuple(peak) in rightToLeft:
                print(f'removing {peak}')
                rightToLeft.remove(tuple(peak))
                continue
            if x_inter < monotonic_stack[len(monotonic_stack)-1]:
                rightToLeft.add(tuple(peak))
                monotonic_stack.append(x_inter)

        monotonic_stack = [float('-inf')]
        leftToRight = set()

        for i in range(0, len(peaks)):
            peak = peaks[i]
            x_inter = peak[0] + peak[1]
            if x_inter > monotonic_stack[len(monotonic_stack)-1]:
                leftToRight.add(tuple(peak))
                monotonic_stack.append(x_inter)
        print(rightToLeft.intersection(leftToRight))
        return len(rightToLeft.intersection(leftToRight))
    
        # Brute force approach
        # def doesOverride(peak1, peak2):
        #     if peak1[1] == peak2[1]:
        #         return peak1[0] == peak2[0]
        #     higherPeak, lowerPeak = (peak1, peak2) if peak1[1] > peak2[1] else (peak2, peak1)
        #     # lower is on left side
        #     if lowerPeak[0] <= higherPeak[0]:
        #         return higherPeak[0] - lowerPeak[0] <= higherPeak[1] - lowerPeak[1]
        #     else:
        #         # lower on right side
        #         return lowerPeak[0] - higherPeak[0]  <= higherPeak[1] - lowerPeak[1]

        # peaks.sort(key = lambda peak: peak[1])
        # curVisiblePeaks = []
        # visiblePeaks = 0
        # peaksVisited = dict()
        # redundantPeaks = set()
        # for peak in peaks:
        #     if tuple(peak) in peaksVisited:
        #         # print('redundant peak')
        #         redundantPeaks.add(tuple(peak))
        #         continue
        #     peaksVisited[tuple(peak)] = True
        #     # print(f'previous visible peaks: {curVisiblePeaks}, curpeak: {peak}')
        #     newVisiblePeaks = []
        #     for visiblePeak in curVisiblePeaks:
        #         # print(f'checking {visiblePeak}')
        #         if not doesOverride(visiblePeak, peak):
        #             # print(f'{peak} does not override {visiblePeak}')
        #             newVisiblePeaks.append(visiblePeak)
        #     curVisiblePeaks = newVisiblePeaks
        #     curVisiblePeaks.append(peak)

        # redundantVisiblePeaks = [redundantPeak for redundantPeak in redundantPeaks if list(redundantPeak) in curVisiblePeaks]

        # return len(curVisiblePeaks) - len(redundantVisiblePeaks)