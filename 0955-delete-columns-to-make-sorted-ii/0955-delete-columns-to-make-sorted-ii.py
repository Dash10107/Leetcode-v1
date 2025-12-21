class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        ans = 0
        n = len(strs);m=len(strs[0])
        fixed=[False]*(n-1)
        for i  in range(m):
            bad = False
            for j in range(n-1):
                if not fixed[j] and strs[j][i]>strs[j+1][i]:
                    bad=True;break
            if bad:
                ans+=1
                continue
            for j in range(n-1):
                if strs[j][i]<strs[j+1][i]:
                    fixed[j]=True
        return ans