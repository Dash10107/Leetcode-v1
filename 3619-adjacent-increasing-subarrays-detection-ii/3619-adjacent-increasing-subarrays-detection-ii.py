class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        inc = [0]*n
        inc[n-1]=1
        for i in range(n-2,-1,-1):
            if nums[i]<nums[i+1]:
                inc[i] = inc[i+1]+1
            else:
                inc[i]=1
            
        def check(mid):
            if n<(2 *mid):return False
            if mid==1:return True
            for i in range(n-(2*mid)+1):
                if inc[i]>=mid and inc[i+mid]>=mid:return True
            return False
        l,r = 1,n//2;ans  = 0
        while l<=r:
            mid = (l+r)//2
            if check(mid):
                ans = mid
                l = mid+1
            else:
                r  = mid-1
        return ans