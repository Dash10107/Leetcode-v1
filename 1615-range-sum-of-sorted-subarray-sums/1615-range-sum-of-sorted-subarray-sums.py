class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        pref = []
        for i in range(n):
            curr=0
            for j in range(i,n):
                curr+=nums[j]
                pref.append(curr)
        pref.sort()
        ans =0;mod=10**9+7
        for ii in range(left-1,right):
            ans =  (pref[ii]+ans)%mod
        return ans%mod