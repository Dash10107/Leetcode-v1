class Router:

    def __init__(self, lim: int):
            self.lim=lim
            self.uniq = set()
            self.q = deque()
            self.dtot=defaultdict(deque)

    def addPacket(self, sor: int, dest: int, ts: int) -> bool:
        pack = (sor,dest,ts)
        if pack in self.uniq:
            return False
        if len(self.q)==self.lim:
            old = self.q.popleft()
            self.uniq.remove(old)
            d = old[1]
            self.dtot[d].popleft()
        self.uniq.add(pack)
        self.q.append(pack)
        self.dtot[dest].append(ts)
        return True

    def forwardPacket(self) -> List[int]:
        if not self.q:return []
        pack = self.q.popleft()
        self.uniq.remove(pack)
        self.dtot[pack[1]].popleft()
        return list(pack)
        

    def getCount(self, dest: int, st: int, et: int) -> int:
        if dest not in self.dtot:return 0
        right = bisect_right(self.dtot[dest],et)
        left = bisect_left(self.dtot[dest],st)
        return right-left


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)