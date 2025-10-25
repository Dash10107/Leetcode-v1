class Solution:
    def maxScore(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        ans=0;pref=0
        for i in range(len(nums)):
            pref+=nums[i]
            if pref>0:ans+=1
        return ans