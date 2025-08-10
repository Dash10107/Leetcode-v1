from typing import List

class Solution:
    def maxTotalReward(self, rewards: List[int]) -> int:
        n = len(rewards)
        rewards.sort()
        max_sum = sum(rewards)  
        dp = [[-1]*(rewards[-1]+1) for i in range(n+1)]
        def func(i, r):
            if r>rewards[-1]:return r
            if i == n:return r
            if dp[i][r] != -1:
                return dp[i][r]
            c = func(i + 1, r)
            if r < rewards[i]:
                c = max(c, func(i + 1, r + rewards[i]))
            dp[i][r] = c
            return c
        return func(0, 0)
