class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre=[1]*n
        suff = [1]*n
        for i in range(1,n):
            pre[i]=pre[i-1]*nums[i-1]
        for j in range(n-2,-1,-1):
            suff[j]=suff[j+1]*nums[j+1]
        ans = [pre[i]*suff[i] for i in range(n)]
        return ans