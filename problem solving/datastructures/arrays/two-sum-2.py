# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
from collections import defaultdict
class Solution:
    def twoSum(self, numbers, target):
        nums_dict = defaultdict(lambda: None)
        for i in range(len(numbers)):
            item = nums_dict[numbers[i]]
            if not item:
                nums_dict[numbers[i]] = [i+1]
            else:
                item.append(i+1)
        for num in numbers:
            if nums_dict[target - num]:
                if target-num == num:
                    if len(nums_dict[target - num]) > 1:
                        return nums_dict[num]
                else:
                    return sorted([nums_dict[target-num][0], nums_dict[num][0]])