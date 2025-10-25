class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ls=0;s=sum(nums)
        ans=[]
        for i in range(n):
            left = (nums[i]*i)-ls
            right = (s-ls)-(nums[i]*(n-i))
            ls+=nums[i]
            ans.append(left+right)
        return ans