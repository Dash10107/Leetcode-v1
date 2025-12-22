class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        m=len(strs[0])
        fixed=[1]*(m)
        for i in range(m-2,-1,-1):
            for j in range(i+1,m):
                for row in strs:
                    if row[i]>row[j]:break
                else:
                    fixed[i]=max(fixed[i],1+fixed[j])
        return m-max(fixed)