class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        c =0 
        n = len(edges)
        vis = [False]*n
        ans = -1
        def func(u,dist):
            vis[u]=True
            neg = edges[u]
            if neg!=-1 and not vis[neg]:
                dist[neg] =  dist[u] + 1
                func(neg,c)
            elif neg!=-1 and neg in dist:
                nonlocal ans
                ans = max(ans,dist[u]-dist[neg]+1)
        for i in range(n):
            if not vis[i]:
                c = defaultdict(int)
                c[i]=1
                func(i,c)
        return ans