class Solution:
    def minimumOperations(self, nums: List[int], target: List[int]) -> int:
        ans,inc,dec=0,0,0
        diff = [nums[i]-target[i] for i in range(len(nums))]
        for i in range(len(nums)):
            if diff[i]>0:
                if inc<diff[i]:
                    ans+= diff[i]-inc
                inc=diff[i]
                dec=0
            elif diff[i]<0:
                if dec<-diff[i]:
                    ans+= (-diff[i]-dec)
                dec = -diff[i]
                inc=0
            else:
                inc=0;dec=0
        return ans