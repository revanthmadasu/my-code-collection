'''
    problem: https://leetcode.com/problems/insert-delete-getrandom-o1/
    concepts: hashtable, arrays, random, math
    performance: 51.5% runtime, 9.39% memory
    todo: improve performance
'''
from collections import defaultdict
import random
import math
class RandomizedSet(object):

    def __init__(self):
        self.vals_reg = defaultdict(lambda: False)

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if self.vals_reg[val]:
            return False
        else:
            self.vals_reg[val] = True
            return True

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if self.vals_reg[val]:
            self.vals_reg.pop(val)
            return True
        else:
            self.vals_reg.pop(val)
            return False

    def getRandom(self):
        """
        :rtype: int
        """
        vals = list(self.vals_reg.keys())
        n = len(vals)
        rand_i = int(math.floor(random.random() * n))
        return vals[rand_i]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()