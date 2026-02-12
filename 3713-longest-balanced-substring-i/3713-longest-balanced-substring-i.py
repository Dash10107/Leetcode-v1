class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s);ans=1
        for i in range(n):
            d = defaultdict(int)
            for j in range(i,n):
                d[s[j]]+=1
                if len(set(d.values()))==1:
                    ans = max(ans,j-i+1)
        return ans