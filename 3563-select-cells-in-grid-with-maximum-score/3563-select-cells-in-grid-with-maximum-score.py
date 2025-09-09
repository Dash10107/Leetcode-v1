class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        
        d = defaultdict(set)
        for r,row in enumerate(grid):
            for val in row:
                d[val].add(r)
        dp = defaultdict(int,{0:0})
        for val in sorted(d)[::-1]:
            for bm in list(dp):
                score = dp[bm]
                for r in d[val]:
                    if not( bm & (1<<r)):
                        dp[bm | (1<<r)]= max(dp[bm|(1<<r)],score+val)
        return max(dp.values())