'''
    problem: https://leetcode.com/problems/integer-to-roman
    concepts: hashtable/hashmap, math
    performance: 30.06% runtime, 54.50% memory
'''
import math
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        cur_num = num
        level_map = {
            3: {
                'l': 'M'
            },
            2: {
                'l': 'C',
                'm': 'D',
                'h': 'M'
            },
            1: {
                'l': 'X',
                'm': 'L',
                'h': 'C'
            },
            0: {
                'l': 'I',
                'm': 'V',
                'h': 'X'
            }
        }
        roman = ''
        while cur_num != 0:
            lvl = math.floor(math.log(cur_num, 10))
            num_digit = int(math.floor(cur_num/math.pow(10, lvl)))
            if num_digit in [1,2,3]:
                roman += level_map[lvl]['l']*num_digit
            elif num_digit == 4:
                roman += level_map[lvl]['l']+level_map[lvl]['m']
            elif num_digit == 5:
                roman += level_map[lvl]['m']
            elif num_digit in [6,7,8]:
                roman += level_map[lvl]['m'] + (level_map[lvl]['l']*(num_digit%5))
            elif num_digit == 9:
                roman += level_map[lvl]['l']+level_map[lvl]['h']
            else:
                roman += level_map[lvl]['h']
            cur_num = cur_num % math.pow(10, lvl)
        return roman