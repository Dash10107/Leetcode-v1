class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u,v,w in edges:
            graph[u].append((v,w))
            graph[v].append((u,2*w))
        dist = [float('inf')]*n
        dist[0]=0
        heap = [(0,0)]
        while heap:
            w,node = heappop(heap)
            if w>dist[node]:continue
            for neg,weg in graph[node]:
                if dist[neg]>dist[node]+weg:
                    dist[neg]=dist[node]+weg
                    heappush(heap,(dist[neg],neg))
        return dist[n-1] if dist[n-1]!=float('inf') else -1