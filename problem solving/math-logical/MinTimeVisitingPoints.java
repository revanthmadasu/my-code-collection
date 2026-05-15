/**
 * Problem: https://leetcode.com/problems/minimum-time-visiting-all-points
 * Concepts: Math, Geometry
 */
import java.lang.Math;
class Solution {
    public int minTimeToVisitAllPoints(int[][] points) {
        int totalTime = 0;
        for (int i=1; i < points.length; ++i) {
            totalTime += getTime(points, i-1, i);
        }
        return totalTime;
    }
    
    int getTime(int[][] points, int pointAI, int pointBI) {
        int absDiffMin = Math.min(Math.abs(points[pointAI][0] - points[pointBI][0]), Math.abs(points[pointAI][1] - points[pointBI][1]));
        int absDiffMax = Math.max(Math.abs(points[pointAI][0] - points[pointBI][0]), Math.abs(points[pointAI][1] - points[pointBI][1]));
        return absDiffMin + (absDiffMax - absDiffMin);
    }
}

