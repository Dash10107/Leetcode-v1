class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0]*n
        st = []
        for j in range(n):
            t = nums[j];c=0
            while st and t>= nums[st[-1]]:
                c= max(c,dp[st.pop()])
            if st:dp[j]=c+1
            else:dp[j]=0
            st.append(j)
        return max(dp)
        
                