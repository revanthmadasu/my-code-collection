'''
    problem: https://leetcode.com/problems/my-calendar-ii/
    concepts: Intervals
    performance: 32.24% runtime, 30.05% memory
'''
class MyCalendarTwo:

    def __init__(self):
        self.doubleBooked = []
        self.allIntervals = []

    def book(self, start: int, end: int) -> bool:
        bookingInterval = (start, end)
        for prevInterval in self.doubleBooked:
            firstInterval, secondInterval = sorted([bookingInterval, prevInterval])
            if firstInterval[0] <= secondInterval[0] and secondInterval[0] < firstInterval[1]:
                return False
        
        for prevInterval in self.allIntervals:
            firstInterval, secondInterval = sorted([bookingInterval, prevInterval])
            if firstInterval[0] <= secondInterval[0] and secondInterval[0] < firstInterval[1]:
                intersectingInterval = (secondInterval[0], min(firstInterval[1], secondInterval[1]))
                self.doubleBooked.append(intersectingInterval)
        self.allIntervals.append(bookingInterval)
        return True
            
                
                

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)
'''
[5, 55], [10, 40]


'''