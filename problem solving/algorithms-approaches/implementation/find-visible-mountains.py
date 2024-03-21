'''
    problem: https://leetcode.com/problems/finding-the-number-of-visible-mountains
    concepts: array, sorting
    #incomplete: timeout error for 2 testcases
    #todo: complete it
'''
from typing import List
class Solution:
    def visibleMountains(self, peaks: List[List[int]]) -> int:
        def doesOverride(peak1, peak2):
            if peak1[1] == peak2[1]:
                return peak1[0] == peak2[0]
            higherPeak, lowerPeak = (peak1, peak2) if peak1[1] > peak2[1] else (peak2, peak1)
            # lower is on left side
            if lowerPeak[0] <= higherPeak[0]:
                return higherPeak[0] - lowerPeak[0] <= higherPeak[1] - lowerPeak[1]
            else:
                # lower on right side
                return lowerPeak[0] - higherPeak[0]  <= higherPeak[1] - lowerPeak[1]

        peaks.sort(key = lambda peak: peak[1])
        curVisiblePeaks = []
        visiblePeaks = 0
        peaksVisited = dict()
        redundantPeaks = set()
        for peak in peaks:
            if tuple(peak) in peaksVisited:
                # print('redundant peak')
                redundantPeaks.add(tuple(peak))
                continue
            peaksVisited[tuple(peak)] = True
            # print(f'previous visible peaks: {curVisiblePeaks}, curpeak: {peak}')
            newVisiblePeaks = []
            for visiblePeak in curVisiblePeaks:
                # print(f'checking {visiblePeak}')
                if doesOverride(visiblePeak, peak):
                    # print(f'{peak} overrides {visiblePeak}')
                    visiblePeaks -= 1
                    # curVisiblePeaks.remove(visiblePeak)
                else:
                    # print(f'{peak} does not override {visiblePeak}')
                    newVisiblePeaks.append(visiblePeak)
            visiblePeaks += 1
            curVisiblePeaks = newVisiblePeaks
            curVisiblePeaks.append(peak)
        # for peak in peaks:
        #     print(doesOverride([15, 39], peak))
        #     print(doesOverride(peak, [15, 39]))
        # print(doesOverride([15, 39], [38, 15]))
        # print(doesOverride([38, 15], [15, 39]))
        redundantVisiblePeaks = [redundantPeak for redundantPeak in redundantPeaks if list(redundantPeak) in curVisiblePeaks]
        # print(f'final visible peaks: {curVisiblePeaks}')
        # print(f'redundant visible peaks: {redundantVisiblePeaks}')
        return len(curVisiblePeaks) - len(redundantVisiblePeaks)