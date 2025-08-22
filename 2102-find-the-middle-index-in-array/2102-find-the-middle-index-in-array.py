class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        n = len(nums)
        pref = [0,nums[0]]
        for i in range(1,n):
            pref.append(pref[-1]+nums[i])
        suff = [0,nums[-1]]
        for i in range(n-2,-1,-1):
            suff.append(suff[-1]+nums[i])
        suff.reverse()
        for i in range(1,n+1):
            if pref[i-1]==suff[i]:
                return i-1        
        return -1