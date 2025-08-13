class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.d = defaultdict(list)
        for i,val in enumerate(arr):
            self.d[val].append(i)

    def query(self, left: int, right: int, val: int) -> int:
        ans = 0
        if val not in self.d:
            return 0 
        pos = self.d[val]
        l = bisect_left(pos,left)
        r = bisect_right(pos,right)
        return r-l


# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)