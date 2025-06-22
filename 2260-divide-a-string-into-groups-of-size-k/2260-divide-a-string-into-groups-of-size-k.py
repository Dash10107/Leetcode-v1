class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        ans = []
        i = 0
        n = len(s)
        while i<n and i+k<=n:
            ans.append(s[i:i+k])
            i+=k
        if n%k!=0:
            ans.append(s[i:]+ (fill*(k-n%k)))
        return ans
