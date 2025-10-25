class Solution:
    def minOperations(self, s1: str, s2: str, x: int) -> int:
        diff = [i for i, (a, b) in enumerate(zip(s1, s2)) if a != b]
        m = len(diff)
        if m % 2: return -1
        @cache
        def func(l,r):
            if l>r:return 0
            if (r-l+1)%2==1:return float('inf')
            k=l+1;ans=float('inf')
            while k<=r:
                cost =min(x,diff[k]-diff[l])
                left = func(l+1,k-1)
                right = func(k+1,r)
                ans = min(ans,cost+left+right)
                k+=2
            return ans
        ans = func(0,m-1)
        return ans if ans<float('inf') else -1