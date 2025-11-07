class MyCalendarTwo:

    def __init__(self):
        self.events =  SortedDict(int)
        

    def book(self, startTime: int, endTime: int) -> bool:
        self.events[startTime] = self.events.setdefault(startTime,0)+1
        self.events[endTime]=self.events.setdefault(endTime,0)-1
        need=0
        for time in self.events:
            need+=self.events[time]
            if need>=3:
                self.events[startTime]-=1
                self.events[endTime]+=1
                return False
        return True



# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)