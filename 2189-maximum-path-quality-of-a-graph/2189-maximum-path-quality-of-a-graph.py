class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        g = defaultdict(list)
        for u,v,t in edges:
            g[u].append((v,t))
            g[v].append((u,t))
        ans = values[0]
        vis = [0]*len(values)
        def dfs(node,t,curr):
            nonlocal ans
            if vis[node]==0:
                curr+= values[node]
            vis[node]+=1
            if node==0:
                ans = max(ans,curr)
            for nei,cost in g[node]:
                if t+cost<=maxTime:
                    dfs(nei,t+cost,curr)
            vis[node]-=1
        dfs(0,0,0)
        return ans