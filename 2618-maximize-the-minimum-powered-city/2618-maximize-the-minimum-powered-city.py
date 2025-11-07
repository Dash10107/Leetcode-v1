class Solution:
    def maxPower(self, nums: List[int], r: int, k: int) -> int:
        n = len(nums)
        pref= [0]*(n+1)
        for i in range(n):
            pref[i+1]=pref[i]+nums[i]
        power = [0]*(n)
        for i in range(n):
            left = max(0,i-r)
            right = min(n-1,i+r)
            power[i]=pref[right+1]-pref[left]
        def ok(x):
            added = [0]*(n+1)
            curr,used=0,0
            for i in range(n):
                curr+=added[i]
                if power[i]+curr<x:
                    need = x-(power[i]+curr)
                    used+=need
                    if used>k:return False
                    curr+=need
                    last = min(n,i+2*r+1)
                    if last<n:added[last]-=need
            return True

        low, high = 0, max(power) + k
        while low < high:
            mid = (low + high + 1) // 2
            if ok(mid):
                low = mid
            else:
                high = mid - 1
        return low