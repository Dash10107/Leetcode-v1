class Solution:
    def maxBalancedShipments(self, weight: List[int]) -> int:
        n = len(weight);i = 0
        ans = 0;m = weight[0]
        for i in range(1,n):
            m = max(weight[i],m)
            if weight[i]<m:
                ans+=1
                if i+1<n:
                    m = weight[i+1]
                else:
                    break
        return ans