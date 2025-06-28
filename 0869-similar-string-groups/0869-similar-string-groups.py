class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        n=len(strs)
        vis=[False]*n
        def sim(a,b):
            c=0
            for i in range(len(a)):
                if a[i]!=b[i]:c+=1
            return c==2 or c==0
        def dfs(u):
            vis[u]=True
            for j in range(n):
                if vis[j]:continue
                if sim(strs[u],strs[j]):
                    dfs(j)
        ans=0
        for i in range(n):
            if not vis[i]:
                dfs(i)
                ans+=1
        return ans