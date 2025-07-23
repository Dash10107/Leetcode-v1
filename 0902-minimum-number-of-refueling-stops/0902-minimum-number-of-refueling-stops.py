class Solution:
    def minRefuelStops(self, target: int, fuel: int, s: List[List[int]]) -> int:
        heap = []
        s = [(0,0)]+s + [(target,0)]
        ans = 0;n = len(s)
        for i in range(1,n):
            fuel-= s[i][0]-s[i-1][0]
            while heap and fuel<0:
                fuel-= heappop(heap)
                ans+=1
            if fuel<0:return -1
            heappush(heap,-s[i][1])
        return ans