class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        suff = n
        ans = 0
        vis = [False]*n
        adj = defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        def dfs(i):
            vis[i] = True
            count = 1
            for neighbor in adj[i]:
                if not vis[neighbor]:
                    count += dfs(neighbor)
            return count
        for i in range(n):
            if not vis[i]:
                count = dfs(i)
                suff-=count
                ans+= suff*count
        return ans