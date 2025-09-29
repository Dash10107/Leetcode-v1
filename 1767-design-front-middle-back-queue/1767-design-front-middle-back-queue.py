class FrontMiddleBackQueue:

    def __init__(self):
        self.arr = deque()

    def pushFront(self, val: int) -> None:
        self.arr.appendleft(val)

    def pushMiddle(self, val: int) -> None:
        mid = len(self.arr)//2
        self.arr.insert(mid,val)

    def pushBack(self, val: int) -> None:
        self.arr.append(val)

    def popFront(self) -> int:
        if not self.arr:return -1
        return self.arr.popleft()

    def popMiddle(self) -> int:
        if not self.arr:return -1
        temp= self.arr[(len(self.arr)-1)//2]
        del  self.arr[(len(self.arr)-1)//2]
        return temp
    def popBack(self) -> int:
        if not self.arr:return -1
        return self.arr.pop()
        


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()