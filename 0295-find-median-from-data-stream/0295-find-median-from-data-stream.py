class MedianFinder:

    def __init__(self):
        self.small=[]
        self.large=[]
        

    def addNum(self, num: int) -> None:
        heappush(self.small,-num)
        if self.small and self.large and -self.small[0]>self.large[0]:
            v = -heappop(self.small)
            heappush(self.large,v)
        if len(self.small)>len(self.large)+1:
            n  = -heappop(self.small)
            heappush(self.large,n)
        if len(self.small)<len(self.large):
            n = -heappop(self.large)
            heappush(self.small,n)

    def findMedian(self) -> float:
        if len(self.small)>len(self.large):
            return -self.small[0]
        return (-self.small[0] + self.large[0])/2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()