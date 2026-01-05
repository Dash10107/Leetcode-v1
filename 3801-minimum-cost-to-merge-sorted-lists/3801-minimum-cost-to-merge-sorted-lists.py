class Solution:
    def minMergeCost(self, lists: List[List[int]]) -> int:
        k = len(lists)
        n = 1<<k
        length = [0]*n
        median = [0]*n
        for mask in range(n):
            merged = []
            for i in range(k):
                if mask & (1<<i):
                    merged.extend(lists[i])
            if merged:
                merged.sort()
                length[mask]=len(merged)
                median[mask]=merged[(len(merged)-1) // 2]
            
        dp = [float('inf')]*n
        for i in range(k):dp[1<<i]=0
        
        for mask in range(n):
            if dp[mask]==0:continue
            s = (mask-1)& mask
            while s:
                t = mask^s
                if t:
                    cost = (dp[s]+dp[t]+length[s]+length[t]+abs(median[s]-median[t]))
                    dp[mask]=min(dp[mask],cost)
                s = (s-1)&mask
        return dp[n-1]

        return 0