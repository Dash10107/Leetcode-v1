class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adj = defaultdict(list)
        for u,v,weight in roads:
            adj[u].append((v,weight))
            adj[v].append((u,weight))
        q =deque([1])
        vis = [False]*(n+1)
        vis[1]=True
        ans = float('inf')
        while q:
            node = q.popleft()
            for v,weight in adj[node]:
                ans = min(ans,weight)
                if not vis[v]:
                    vis[v]=True
                    q.append(v)
        return ans