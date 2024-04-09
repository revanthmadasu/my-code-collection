'''
    Problem: https://leetcode.com/problems/logger-rate-limiter/
    Concepts: Design, Stream, Hashtable
    performance: 90.03% runtime, 60.66% memory
'''
class Logger:

    def __init__(self):
        self.messageTimestamps = dict()

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        curTimestamp = self.messageTimestamps[message] if message in self.messageTimestamps else 0
        if curTimestamp <= timestamp:
            self.messageTimestamps[message] = timestamp + 10
            return True
        else:
            return False
