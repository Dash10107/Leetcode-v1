class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        c = Counter(nums)
        m = max(nums).bit_length()
        full = (1<<m)-1
        n = 1<<m
        dp = [(0, 0)] * n
        def add(mask,val):
            a,b  = dp[mask]
            if val>a:
                if val!=a:dp[mask]=(val,a)
            elif val>b and val!=a:
                dp[mask]=(a,val)
                
        for v in c:
            add(v,v)
        for i in range(m):
            bit = 1<<i
            for mask in range(n):
                if mask&bit:
                    o = mask^bit
                    a,b= dp[o]
                    if a:add(mask,a)
                    if b:add(mask,b)
                    
        ans = 0
        for v,cc in c.items():
            ch= full^v
            a,b = dp[ch]
            if a and (a!=v or cc>1):
                ans = max(ans,v*a)
            elif b:
                ans = max(ans,v*b)
        return ans