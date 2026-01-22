class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        ans = 0
        while True:
            s=True
            for i in range(len(nums)-1):
                if nums[i]>nums[i+1]:
                    s=False;break
            if s:return ans
            ms,mi = float('inf'),-1
            for i in range(len(nums)-1):
                if nums[i]+nums[i+1]<ms:
                    ms = nums[i]+nums[i+1]
                    mi = i
            new = nums[:mi]+[ms]+nums[mi+2:]
            nums = new
            ans+=1
        return ans