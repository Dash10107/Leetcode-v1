class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        s = set()
        n = len(nums);ans=0;i=0;j=0
        ss = 0
        while i<n:
            while j<i and nums[i] in s:
                s.remove(nums[j])
                ss-=nums[j]
                j+=1
            s.add(nums[i])
            ss+=nums[i]
            ans = max(ans,ss)
            i+=1
        return ans