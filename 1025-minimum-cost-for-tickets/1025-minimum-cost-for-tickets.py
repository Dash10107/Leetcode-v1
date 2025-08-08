class Solution:
    def __init__(self):
        self.dp = [-1]*366
    def lower_bound(self,arr,target):
        l,r = 0,len(arr)
        while l<r:
            mid = (l+r)//2
            if arr[mid]>=target:
                r = mid
            else:
                l = mid+1
        return l
    
    def solve(self,ind,days,costs):
        if ind>=len(days):
            return 0
        if self.dp[ind]!=-1:
            return self.dp[ind]
        oneDay = costs[0] + self.solve(ind + 1, days, costs)

        sevenDayIndex = self.lower_bound(days, days[ind] + 7)
        sevenDays = costs[1] + self.solve(sevenDayIndex, days, costs)

        thirtyDayIndex = self.lower_bound(days, days[ind] + 30)
        thirtyDays = costs[2] + self.solve(thirtyDayIndex, days, costs)

        self.dp[ind] = min(oneDay, min(sevenDays, thirtyDays))
        return self.dp[ind]
        
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        self.dp = [-1] * 366
        return self.solve(0, days, costs)