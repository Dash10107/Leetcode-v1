class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        ans = 0
        n = len(startTime)
        duration = [endTime[i]-startTime[i] for i in range(n)]
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i+1] = prefix[i] + duration[i]
        for i in range(n-k+1):
            left = endTime[i-1] if i>0 else 0
            right = startTime[i+k] if i+k<n else eventTime
            gap = right - left - (prefix[i + k] - prefix[i])
            ans = max(ans,gap)
        return ans