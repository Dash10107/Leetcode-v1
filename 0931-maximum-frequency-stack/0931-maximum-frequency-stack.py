class FreqStack:

    def __init__(self):
        self.groups = defaultdict(list)
        self.freq = defaultdict(int)
        self.m = 0

    def push(self, val: int) -> None:
        f = self.freq[val]+1
        self.freq[val]=f
        self.m = max(f,self.m)
        self.groups[f].append(val)
        

    def pop(self) -> int:
        val = self.groups[self.m].pop()
        self.freq[val]-=1
        if not self.groups[self.m]:
            self.m-=1
        return val
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()