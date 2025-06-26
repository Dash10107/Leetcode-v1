class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        dp = [0]
        for c in reversed(s):
            t = 0 if c=='0' else 1
            if t:
                dp.append(dp[-1]+ 2**(len(dp)-1))
            else:
                dp = [0]+dp
        for i in range(len(dp)-1,-1,-1):
            if dp[i]<=k:
                return i