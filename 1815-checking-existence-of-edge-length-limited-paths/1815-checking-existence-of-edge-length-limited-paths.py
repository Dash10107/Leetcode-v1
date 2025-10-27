class DSU:
    def __init__(self,n):
        self.parent=list(range(n))
        self.rank=[0]*n
    
    def find(self,x):
        if self.parent[x]!=x:
            self.parent[x]=self.find(self.parent[x])
        return self.parent[x]
    
    def union(self,x,y):
        px,py=self.find(x),self.find(y)
        if px==py:
            return False
        if self.rank[px]<self.rank[py]:
            self.parent[px]=py
        elif self.rank[py]>self.rank[px]:
            self.parent[py]=px
        else:
            self.parent[py]=px
            self.rank[px]+=1
        return True

class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        dsu = DSU(n)
        for i in range(len(queries)):queries[i].append(i)
        queries.sort(key=lambda x:x[2])
        edgeList.sort(key=lambda x:x[2])
        ans = [False]*len(queries)
        i=0;n=len(edgeList)
        for p,q,l,j in queries:
            while i<n and edgeList[i][2]<l:
                dsu.union(edgeList[i][0],edgeList[i][1])
                i+=1
            if dsu.find(p)==dsu.find(q):
                ans[j]=True
        return ans