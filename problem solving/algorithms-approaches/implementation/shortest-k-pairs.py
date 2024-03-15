'''
    problem: https://leetcode.com/problems/find-k-pairs-with-smallest-sums/
    # todo: 4 testcases failing
'''
from typing import List

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        p1, p2 = 0, 0
        n1, n2 = len(nums1), len(nums2)
        c = 0
        res = []
        c_map1 = dict()
        c_map2 = dict()

        while c < k and p1 < n1 and p2 < n2:
            print(f'p1: {p1}, p2: {p2}')
            res.append((nums1[p1], nums2[p2]))
            # c_map1[p1] = max(p2, c_map1[p1]) if p1 in c_map1 else p2
            # c_map2[p2] = max(p1, c_map2[p2]) if p2 in c_map2 else p1
            c_map1[p1] = p2
            c_map2[p2] = p1
            c += 1
            comb1, comb2 = float('inf'), float('inf')
            c1_p1, c1_p2, c2_p1, c2_p2 = None, None, None, None
            for i in range(0, min(n1-1, p1+1)+1):
                _exit = False
                if i in c_map1:
                    # get next p2
                    n_p2 = c_map1[i]+1
                else:
                    n_p2 = 0
                    _exit = True
                if n_p2 < n2:
                    if comb1 > (nums1[i] + nums2[n_p2]):
                        comb1 = nums1[i] + nums2[n_p2]
                        c1_p1 = i
                        c1_p2 = n_p2
                if _exit:
                    break
            for i in range(0, min(n2-1, p2+1)+1):
                _exit = False
                if i in c_map2:
                    # get next p1
                    n_p1 = c_map2[i]+1
                else:
                    n_p1 = 0
                    _exit = True
                if n_p1 < n1:
                    if comb2 > (nums1[n_p1] + nums2[i]):
                        comb1 = nums1[n_p1] + nums2[i]
                        c2_p1 = n_p1
                        c2_p2 = i
                if _exit:
                    break

            if comb1 < comb2:
                print(f'selecting b1: {c1_p1}, {c1_p2} => {comb1}')
                p1 = c1_p1
                p2 = c1_p2
            else:
                print(f'selecting b2: {c2_p1}, {c2_p2} => {comb2}')
                p1 = c2_p1
                p2 = c2_p2
            # mapped_p1 = (c_map1[p2]+1 if (p2 in c_map1) and c_map1[p2]+1 < n1 else 0)
            # mapped_p2 = (c_map2[p1]+1 if (p1 in c_map2) and c_map2[p1]+1 < n2 else 0)
            # if (p1+1) < n1:
            #     if (p2+1) < n2:
            #         if (nums1[p1] + nums2[mapped_p2]) < (nums1[mapped_p1] + nums2[p2]):
            #         # if nums1[p1+1] < nums2[p2+1]:
            #             # p1 += 1
            #             p2 = mapped_p2
            #         else:
            #             # p2 += 1
            #             p1 = mapped_p1
            #     # no more element in nums2
            #     else:
            #         # p1 += 1
            #         p2 = mapped_p2
            # # no more element in nums1
            # elif (p2+1) < n2:
            #     # p2 += 1
            #     p1 = mapped_p1
            # else:
            #     break
        return res
    
sol = Solution()

# print(sol.kSmallestPairs([1,2,4,5,6], [3,5,7,9], 3))
print(sol.kSmallestPairs([1,2,4,5,6], [3,5,7,9], 20))