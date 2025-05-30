class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        adj = [[] for i in range(n)]
        for i in range(n):
            x,y,r = bombs[i]
            for j in range(n):
                if i!=j:
                    x1,y1,_ = bombs[j]
                    dx,dy = x-x1,y-y1
                    if dx*dx + dy*dy<=r*r:
                        adj[i].append(j)
        def dfs(node,vis):
            vis.add(node)
            for ne in adj[node]:
                if ne not in vis:
                    dfs(ne,vis)
        ans = 0
        for i in range(n):
            vis = set()
            dfs(i,vis)
            ans = max(ans,len(vis))
        return ans