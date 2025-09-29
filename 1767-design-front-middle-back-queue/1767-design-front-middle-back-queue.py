class FrontMiddleBackQueue:

    def __init__(self):
        self.front = deque()
        self.back = deque()

    def pushFront(self, val: int) -> None:
        self.front.appendleft(val)
        self.rebalance()

    def pushMiddle(self, val: int) -> None:
        if len(self.front)>len(self.back):
            self.back.appendleft(self.front.pop())
        self.front.append(val)
        self.rebalance() 

    def pushBack(self, val: int) -> None:
        self.back.append(val)
        self.rebalance()

    def popFront(self) -> int:
        if not self.front :return -1
        t= self.front.popleft()
        self.rebalance()
        return t

    def popMiddle(self) -> int:
        if not self.front:return -1
        t = self.front.pop()
        self.rebalance()
        return t

    def popBack(self) -> int:
        if not self.front and not self.back:return -1
        if self.back:
            t =  self.back.pop()
        else:
            t = self.front.pop()
        self.rebalance()
        return t
    def rebalance(self):
        if len(self.front)<len(self.back):
            self.front.append(self.back.popleft())
        elif len(self.front)>len(self.back)+1:
            self.back.appendleft(self.front.pop())


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()