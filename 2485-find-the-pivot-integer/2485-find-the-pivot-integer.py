class Solution:
    def pivotInteger(self, n: int) -> int:
        suff = [0]*(n+2)
        for i in range(n,0,-1):
            suff[i]=suff[i+1]+i
        pref = 0
        for i in range(1,n+1):
            pref+=i
            if pref==suff[i]:
                return i
        return -1