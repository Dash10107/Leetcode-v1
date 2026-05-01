class Solution:
    def kthRemainingInteger(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        n=len(nums)
        pref=[0]*n;eso=0
        for i,ni in enumerate(nums):
            if ni%2==0:eso+=1
            pref[i]=eso
        def q(l,r):
            if l==0:return pref[r]
            return pref[r]-pref[l-1]
        def g(t,l,r):
            ec=t//2
            if t>=nums[r]:
                d=q(l,r)
                return ec-d
            if t<nums[l]:return ec
            last = bisect_right(nums,t)
            return ec-q(l,last-1)
        res=[]
        for l,r,k in queries:
            ll=1;rr=10**14
            ans=-1
            while ll<=rr:
                mid = (ll+rr)//2
                if g(mid,l,r)>=k:
                    ans=mid
                    rr=mid-1
                else:
                    ll=mid+1
            res.append(ans)
        return res