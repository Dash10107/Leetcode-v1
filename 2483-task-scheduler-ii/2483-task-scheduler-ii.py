class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        n = len(tasks)
        c = defaultdict(int)
        rep=False
        ans=1
        for t in tasks:
            last = c.get(t,0)
            if last!=0 and last+space+1>ans:
                wait = last+space-ans+1
                ans+=wait
                rep=True
                c[t]=ans                
            else:
                ans+=1
                c[t]=ans
        return  ans-1