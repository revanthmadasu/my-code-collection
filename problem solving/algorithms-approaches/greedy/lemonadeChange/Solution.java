/*
    problem: https://leetcode.com/problems/lemonade-change
    concepts: Arrays, Greedy
    performance: 95.27% runtime, 48.09% memory
*/
class Solution {
    public boolean lemonadeChange(int[] bills) {
        int c10 = 0, c5 = 0;
        for (int bill: bills) {
            if (bill == 5) {
                c5 += 1;
            } else if (bill == 10) {
                if (c5 > 0) {
                    c5 -= 1;
                    c10 += 1;
                } else {
                    return false;
                }
            } else if (bill == 20) {
                if (c5 * 5 + c10 * 10 >= 15 && c5 > 0) {
                    if (c10 > 0) {
                        c10 -= 1;
                        c5 -= 1;
                    } else {
                        c5 -= 3;
                    }
                } else {
                    return false;
                }
            }
        }
        return true;
    }
}