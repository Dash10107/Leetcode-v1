class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        edges.sort(key=lambda x:max(vals[x[0]],vals[x[1]]))
        n = len(vals)
        par = list(range(n));size = [1]*n
        def find(i):
            if par[i]!=i:
                par[i]=find(par[i])
            return par[i]
        ans = n
        for u,v in edges:
            paru,parb =  find(u),find(v)
            if vals[paru]==vals[parb]:
                ans+= size[paru]*size[parb]
                par[paru]=parb
                size[parb]+=size[paru]
            elif vals[paru]>vals[parb]:
                par[parb]=paru
            else:
                par[paru]=parb
        return ans