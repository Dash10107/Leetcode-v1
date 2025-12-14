class Solution:
    def minMoves(self, balance: List[int]) -> int:
        s = sum(balance)
        if s<0:return -1
        idx = -1
        for i,n in enumerate(balance):
            if n<0:
                idx=i;break
        if idx==-1:return 0
        n = len(balance)
        need = -balance[idx]
        ans=0;d=1
        l,r = (idx-1)%n,(idx+1)%n
        while need>0:
            if balance[l]>0:
                take = min(balance[l],need)
                ans+= (take*d)
                need-=take
            if need==0:break
            if balance[r]>0:
                take = min(balance[r],need)
                ans+= (take*d)
                need-=take
            l = (l-1)%n
            r = (r+1)%n
            d+=1
        return ans
