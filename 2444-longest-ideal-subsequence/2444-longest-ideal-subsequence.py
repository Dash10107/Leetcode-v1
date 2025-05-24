class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp = [0] * 128  # ASCII characters
        for c in s:
            idx = ord(c)
            best = 0
            for j in range(max(0, idx - k), min(127, idx + k) + 1):
                best = max(best, dp[j])
            dp[idx] = best + 1
        return max(dp)
