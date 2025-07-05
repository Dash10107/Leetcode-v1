class Solution:
    def checkArray(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        pref = [0]*(n+1)
        nc = 0
        for i in range(0,n):
            nc-=pref[i]
            nums[i]-=nc
            if nums[i]<0:
                return False
            if i+k<=n:
                nc+=nums[i]
                pref[i+k]+= nums[i]
                nums[i]=0
            elif nums[i]>0:
                return False
        return True