class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref = [0]*(n+1)
        for i in range(n):
            pref[i+1]=pref[i]+nums[i]
        suff = [0]*(n+1)
        for i in range(n-1,-1,-1):
            suff[i]=suff[i+1]+nums[i]
        ans = []
        for i in range(n):
            left = (nums[i]*i)-pref[i]
            right = suff[i]- (nums[i]*(n-i))
            ans.append(left+right)
        return ans