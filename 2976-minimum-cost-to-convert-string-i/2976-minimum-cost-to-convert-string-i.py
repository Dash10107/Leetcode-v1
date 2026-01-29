class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        dp = [[float('inf')]*26 for _ in range(26)]
        for og,ch ,co in zip(original,changed,cost):
            st = ord(og)-ord('a');en = ord(ch)-ord('a')
            dp[st][en]=min(dp[st][en],co)
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    dp[i][j]=min(dp[i][j],dp[i][k]+dp[k][j])
        ans = 0
        for s,t in zip(source,target):
            if s!=t:
                st = ord(s)-ord('a');en = ord(t)-ord('a')
                if dp[st][en]==float('inf'):
                    return -1
                else:
                    ans+=dp[st][en]
        return ans        