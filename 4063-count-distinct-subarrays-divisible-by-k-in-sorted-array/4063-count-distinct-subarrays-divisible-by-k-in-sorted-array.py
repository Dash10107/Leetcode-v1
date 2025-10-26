from math import lcm

class Solution:
    def numGoodSubarrays(self, nums: List[int], k: int) -> int:
        s = 0
        dp = {0: 1}
        ans = 0
        cnts = 0
        prev = None

        for i in nums:
            if i == prev:
                cnts += 1
            else:
                cnts = 1
                prev = i
            
            fact = lcm(k, i) // i
            
            subt = cnts // fact
            if cnts % fact == 0:
                subt -= 1
            
            s = (s + i) % k
            
            if s not in dp:
                dp[s] = 0
                
            ans += dp[s] - subt
            dp[s] += 1
            
        return ans