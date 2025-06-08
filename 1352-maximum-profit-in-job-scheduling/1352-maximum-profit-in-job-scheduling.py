class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        
        # DP will store tuples of (end time, max profit up to that time)
        dp = [(0, 0)]  # (endTime, profit)

        for s, e, p in jobs:
            # Binary search to find the latest job that ends <= current start time
            i = bisect_right(dp, (s, float('inf'))) - 1
            curr_profit = dp[i][1] + p

            if curr_profit > dp[-1][1]:
                dp.append((e, curr_profit))

        return dp[-1][1]