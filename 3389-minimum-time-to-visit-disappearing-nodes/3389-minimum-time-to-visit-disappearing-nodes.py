class Solution:
    def minimumTime(self, n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:
        g = defaultdict(list)
        for u,v,w in edges:
            g[u].append((v,w))
            g[v].append((u,w))
        dist = [-1]*n
        vis = [False]*n
        heap = [(0,0)]
        dist[0]=0
        while heap:
            d,node = heappop(heap)
            if vis[node] or d>=disappear[node]:
                continue
            dist[node]=d
            vis[node]=True
            for neg,w in g[node]:
                if not vis[neg]:
                    heappush(heap,(d+w,neg))
        return dist