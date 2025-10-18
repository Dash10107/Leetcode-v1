class MyCalendarThree:

    def __init__(self):
        self.time = Counter()
        self.ans=0

    def book(self, startTime: int, endTime: int) -> int:
        self.time[startTime]+=1
        self.time[endTime]-=1
        curr = 0
        for t in sorted(self.time):
            curr+=self.time[t]
            self.ans=max(self.ans,curr)
        return self.ans