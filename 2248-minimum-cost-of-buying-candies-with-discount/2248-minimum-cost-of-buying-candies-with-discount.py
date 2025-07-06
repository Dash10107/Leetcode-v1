class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        ans = 0
        i = 0;n=len(cost)
        while i<n:
            s = cost[i]
            if i+1<n:
                s+=cost[i+1]
            ans +=s
            if i+3<n:
                i+=3
            else:
                break
        return ans