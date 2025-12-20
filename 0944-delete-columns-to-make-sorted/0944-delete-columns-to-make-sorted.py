class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        ans = 0
        cols = defaultdict(str)
        n = len(strs);m=len(strs[0])
        for i  in range(m):
            for j in range(n):
                cols[i]+=strs[j][i]
    
        for s in cols.values():
            
            if s!= ''.join(sorted(s)):ans+=1
        return ans