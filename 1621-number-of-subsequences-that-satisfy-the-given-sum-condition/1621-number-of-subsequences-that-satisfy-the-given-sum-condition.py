class Solution:
    def numSubseq(self, arr: List[int], target: int) -> int:
        mod = 10**9+7
        arr.sort()
        n = len(arr)
        ans = 0
        l,r =0,n-1
        while l<=r:
            if arr[l]+arr[r]<=target:
                ans +=  ((2**(r-l))%mod)
                l+=1
            else:
                r-=1
        return ans%mod
