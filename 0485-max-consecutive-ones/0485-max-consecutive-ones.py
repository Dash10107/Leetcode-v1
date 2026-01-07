class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        res = 0
        for n in nums:
            if n==1:
                ans+=1
            else:
                ans=0
            res = max(ans,res)
        return res