class StockSpanner:

    def __init__(self):
        self.arr = []
        

    def next(self, price: int) -> int:
        c=1
        while self.arr and self.arr[-1][0]<=price:
            _,p = self.arr.pop()
            c+=p
        self.arr.append((price,c))
        return c
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)