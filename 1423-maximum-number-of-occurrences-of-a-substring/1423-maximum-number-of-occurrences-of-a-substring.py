class Solution:
    def maxFreq(self, s: str, maxl: int, mins: int, maxs: int) -> int:
        n = len(s);ans = defaultdict(int)
        res = 0
        for i in range(n):
            for j in range(i+mins-1,i+maxs):
                if j<n:
                    t = s[i:j+1]
                    
                    if len(set(t))<=maxl:
                        ans[t]+=1
                        res = max(res,ans[t]) 
                         
        return res