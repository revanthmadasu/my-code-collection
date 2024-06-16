'''
    Problem: https://leetcode.com/problems/time-based-key-value-store/
    Concepts: Binary Search, Searching, Hashtable
    performance: 20.40% runtime, 80.57% memory
    #insight: similiar question was asked in google interview in march - history set
'''
class TimeMap:

    def __init__(self):
        self.keysDict = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.keysDict:
            self.keysDict[key] = []
        self.keysDict[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keysDict:
            return ""
        values = self.keysDict[key]
        left, right = 0, len(values)-1
        if values[left][0] > timestamp:
            return ""
        res = ""
        while left != right:
            if values[left][0] > timestamp:
                return res
            res = values[left][1]
            mid = (left + right) // 2
            if values[mid][0] == timestamp:
                return values[mid][1]
            elif values[mid][0] > timestamp:
                right = mid
            else:
                left = mid + 1
        if values[left][0] > timestamp:
            return res
        else:
            return values[left][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)