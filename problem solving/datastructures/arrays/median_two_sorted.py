'''
    https://leetcode.com/problems/median-of-two-sorted-arrays/description/
    Concept: Arrays, Sorting
'''
class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        len_nums1 = len(nums1)
        len_nums2 = len(nums2)
        primary, len_primary, secondary, len_secondary = [nums1, len_nums1, nums2, len_nums2] if len_nums1 > len_nums2 else [nums2, len_nums2, nums1, len_nums1]
        p_i = 0
        s_i = 0
        merged = []
        len_merged = 0
        def loadAll(arr, len_arr, i, res):
            while i < len_arr:
                res.append(arr[i])
                i += 1
        while len_merged < (len_primary+len_secondary):
            print(p_i, s_i)
            if s_i >= len_secondary:
                loadAll(primary, len_primary, p_i, merged)
            elif p_i >= len_primary:
                loadAll(secondary, len_secondary, s_i, merged)
            elif primary[p_i] < secondary[s_i]:
                merged.append(primary[p_i])
                p_i += 1
            else:
                merged.append(secondary[s_i])
                s_i += 1
            len_merged += 1
        return ((merged[int(len_merged/2)] + merged[int(len_merged/2)-1])/2)if len_merged % 2 == 0 else merged[int(len_merged/2)]