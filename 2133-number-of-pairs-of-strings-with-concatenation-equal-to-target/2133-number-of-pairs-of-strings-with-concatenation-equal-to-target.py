class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        n = len(nums);ans=0
        for i in range(n):
            for j in range(i+1,n):
                if nums[i]+nums[j]==target:
                    ans+=1
                if nums[j]+nums[i]==target:
                    ans+=1
        return ans