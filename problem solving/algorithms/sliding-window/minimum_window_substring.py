'''
    Problem: https://leetcode.com/problems/minimum-window-substring/
    concepts: Sliding Window, Two Pointers, Hash Table, String
    performance: 78.91% runtime, 66.14% memory
'''
import math
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need_map = {}
        have_map = {}
        for ch in t:
            if ch not in need_map:
                need_map[ch] = 0
            need_map[ch] = need_map[ch] + 1
            have_map[ch] = 0
        satisfied_counts = 0
        all_counts = len(need_map)

        n = len(s)
        result = (-1, -1, math.inf)
        left = 0
        right = -1
        while right < n:
            # print(f'1 {have_map}, r: {right}, l: {left}, ss: {s[left:right+1]} res: {result}')
            satisfied = satisfied_counts == all_counts
            # if current window does not have string expand right - look for new character if it satisfies or not
            if not satisfied:
                # print("not satisfied")
                right += 1
                if right >= n:
                    break
                r_ch = s[right]
                if r_ch in need_map:
                    have_map[r_ch] += 1
                    if need_map[r_ch] == have_map[r_ch]:
                        satisfied_counts += 1
                    if satisfied_counts == all_counts:
                        # print(f"all counts satisfied,l: {left}, r: {right}, ss: {s[left: right+1]} ")
                        if result[2] > right-left:
                            result = (left, right, right-left)
            else:
                # print('satisfied')
                l_ch = s[left]
                left += 1
                if l_ch in need_map:
                    have_map[l_ch] -= 1
                    if need_map[l_ch] > have_map[l_ch]:
                        satisfied_counts -= 1

                if satisfied_counts == all_counts:
                    # print(f"all counts satisfied,l: {left}, r: {right}, ss: {s[left: right+1]} ")
                    if result[2] > right-left:
                        result = (left, right, right-left)
            # print(f'2 {have_map}, r: {right}, l: {left}, ss: {s[left:right+1]} res: {result}')
        if result[2] == math.inf:
            return ""
        else:
            return s[result[0]:result[1]+1]
        