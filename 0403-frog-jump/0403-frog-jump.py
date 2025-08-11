class Solution:
    def canCross(self, stones: List[int]) -> bool:
        n = len(stones)
        dp = defaultdict(set)
        dp[1]={1}
        for loc in stones[1:]:
            for s in list(dp[loc]):
                dp[loc+s].add(s)
                dp[loc+s-1].add(s-1)
                dp[loc+s+1].add(s+1)
        return len(dp[stones[-1]])!=0