class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        d = deque()
        s = 0;i=0;n=len(chargeTimes);ans=0
        target= budget
        for j in range(n):
            while d and chargeTimes[d[-1]]<chargeTimes[j]:
                d.pop()
            s+=runningCosts[j]
            d.append(j)
            target = chargeTimes[d[0]]+ ((j-i+1)*s)
            while i<=j and target>budget:
                if d and d[0]==i:
                    d.popleft()
                s-=runningCosts[i]
                i+=1
                m = chargeTimes[d[0]] if d else 0
                target = m+((j-i+1)*s)
            ans = max(ans,j-i+1)
        return ans