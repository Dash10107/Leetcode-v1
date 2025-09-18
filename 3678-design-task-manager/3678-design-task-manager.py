class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.ttou = {};self.ttop={}
        self.heap = []
        for u,t,p in tasks:
            self.ttou[t]=u
            self.ttop[t]=p
            heappush(self.heap,(-p,-t))      

    def add(self, u: int, t: int, p: int) -> None:
        self.ttou[t]=u
        self.ttop[t]=p
        heappush(self.heap,(-p,-t))
        

    def edit(self, taskId: int, new: int) -> None:
        self.ttop[taskId]=new
        heappush(self.heap,(-new,-taskId))
        

    def rmv(self, taskId: int) -> None:
        self.ttou.pop(taskId, None)
        self.ttop.pop(taskId, None)

        

    def execTop(self) -> int:
        while self.heap:
            p,t = heappop(self.heap)
            if (-t in self.ttou) and (-t in self.ttop) and self.ttop[-t] == -p:
                u =self.ttou[-t]
                self.ttou.pop(-t, None)
                self.ttop.pop(-t, None)
                return u
        return -1


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()