class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        mod = 10**9+7
        dp = [0]*(len(nums)+1)
        pref = [0]*(len(nums)+1)
        dp[0]=1
        pref[0]=1
        l = 0
        dqmi,dqma = deque(),deque()
        for i in range(len(nums)):
            while dqma and dqma[-1]<nums[i]:
                dqma.pop()
            dqma.append(nums[i])
            while dqmi and dqmi[-1]>nums[i]:
                dqmi.pop()
            dqmi.append(nums[i])
            while  dqma[0]-dqmi[0]>k:
                if nums[l]==dqma[0]:
                    dqma.popleft()
                if nums[l]==dqmi[0]:
                    dqmi.popleft()
                l+=1
            temp = pref[i]
            if l>0:
                temp = (temp-pref[l-1])%mod
            dp[i+1]=temp
            pref[i+1]=(pref[i]+dp[i+1])%mod
        return dp[len(nums)]