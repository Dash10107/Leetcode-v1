class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        dp =defaultdict(int)
        def func(ind):
            if ind in dp:return dp[ind]
            m = 0
            for j in range(ind+1,ind+d+1):
                if j>=len(arr) or arr[j]>=arr[ind]:break
                m = max(m,func(j))
            for j in range(ind-1,ind-d-1,-1):
                if j<0 or arr[j]>=arr[ind]:break
                m = max(m,func(j))
            dp[ind] = m+1
            return dp[ind]
        ans = 0
        for i in range(len(arr)):
            ans = max(ans,func(i))
        return ans