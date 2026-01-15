class SORTracker:

    def __init__(self):
        self.s=[]
        self.i=0

    def add(self, name: str, score: int) -> None:
        insort(self.s,(-score,name))

    def get(self) -> str:
        _,name = self.s[self.i]
        self.i+=1
        return name



# Your SORTracker object will be instantiated and called as such:
# obj = SORTracker()
# obj.add(name,score)
# param_2 = obj.get()