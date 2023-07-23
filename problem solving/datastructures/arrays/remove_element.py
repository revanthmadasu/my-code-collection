'''
    problem: https://leetcode.com/problems/remove-element
    concepts: arrays, two pointers
    runtime: 84.33% memory: 73.8%
'''
class Solution:
    # low performance: runtime: 17.6% memory: 37.8%
    # def removeElement(self, nums: List[int], val: int) -> int:
    #     res_nums = []
    #     for num in nums:
    #         if num != val:
    #             res_nums.append(num)
    #     k = len(res_nums)
    #     for i in range(k):
    #         nums[i] = res_nums[i]
    #     return k  

    # 
    def removeElement(self, nums: List[int], val: int) -> int:   
        n = len(nums)    
        p1 , p2 = (0, 0)
        k = 0
        if not n:
            return 0
        while p2 < n:
            # print(f'initial p1: {p1} p2: {p2}')
            while p2 < n and nums[p2] == val:
                # print(f'skipping {p2}')
                p2 += 1
                k+=1 
            # print(f'after skipping p1: {p1} p2: {p2}')
            if p2 >= n:
                break
            nums[p1] = nums[p2]
            p1+=1
            p2+=1
        return n-k      