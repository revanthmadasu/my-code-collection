/*
    problem: https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts
    concepts: Arrays, Sorting
    performance: 92.20% runtime, 50.24% memory
*/
package MaxAreaAfterCuts;

import java.util.Arrays;
class Solution {
    public int maxArea(int h, int w, int[] horizontalCuts, int[] verticalCuts) {
        Arrays.sort(horizontalCuts);
        Arrays.sort(verticalCuts);
        int prevRow = 0;
        int maxRowWidth = 0;
        for (int hCut: horizontalCuts) {
            maxRowWidth = Math.max(maxRowWidth, hCut - prevRow);
            prevRow = hCut;
        }
        int prevCol = 0;
        int maxColWidth = 0;
        for (int vCut: verticalCuts) {
            maxColWidth = Math.max(maxColWidth, vCut - prevCol);
            prevCol = vCut;
        }
        long MODULO = 1000000007;
        maxColWidth = Math.max(maxColWidth, w - prevCol);
        maxRowWidth = Math.max(maxRowWidth, h - prevRow);
        return (int)(((long)maxColWidth * (long)maxRowWidth) % MODULO);
    }
}