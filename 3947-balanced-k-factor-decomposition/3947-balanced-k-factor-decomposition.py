class Solution:
    def minDifference(self, n: int, k: int) -> List[int]:
        facs = []
        for p in range(1,int(sqrt(n))+1):
            if n%p==0:
                facs.append(p)
                if p != n//p:
                    facs.append(n//p)
        facs.sort()
        ans,diff=None,float('inf')
        def func(rem,pick,path):
            nonlocal ans,diff
            if pick==1:
                cand = path + [rem]
                if all (cand[i]<= cand[i+1] for i in range(len(cand)-1)):
                    d = max(cand)-min(cand)
                    if d<diff:
                        ans,diff = cand,d
                return
            for d in facs:
                if rem%d==0 and (not path or d>=path[-1]):
                    func(rem//d,pick-1,path+[d])
        func(n,k,[])
        return ans