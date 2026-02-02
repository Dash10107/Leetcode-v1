class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        k-=1
        win = SortedList(nums[1:dist+2])
        curr = sum(win[:k])
        ans = curr;n=len(nums)
        for i in range(1,n-dist-1):
            out = nums[i];inn=nums[i+dist+1]
            io = win.index(out)
            if io<k:
                curr-=out
                if k < len(win): 
                    curr+=win[k]
            win.remove(out)
            win.add(inn)
            iin = win.index(inn)
            if iin<k:
                curr+=inn
                if k < len(win):
                    curr-=win[k]
            ans = min(ans,curr)
        return ans+nums[0]