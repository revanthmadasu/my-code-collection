'''
    Problem: https://leetcode.com/problems/validate-ip-address/
    Concepts: String
    performance: 92.07% runtime, 86.28% memory
'''
class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        def isIpV4():
            parts = queryIP.split('.')
            if len(parts) != 4:
                return False
            for part in parts:
                # leading zeros
                if (len(part) > 1 and part[0] == '0') or len(part) == 0:
                    return False
                # number
                if not part.isnumeric():
                    return False
                if int(part) > 255:
                    return False
            return True
        def isIpV6():
            parts = queryIP.split(':')
            if len(parts) != 8:
                return False
            for part in parts:
                if len(part) < 1 or len(part) > 4:
                    return False
                try:
                    num = int(part, 16)
                except:
                    return False
            return True
        if isIpV4():
            return "IPv4"
        elif isIpV6():
            return "IPv6"
        else:
            return "Neither"