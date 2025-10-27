class Solution:
    def findAnswer(self, n: int, edges: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        for u,v,w in edges:
            graph[u].append((v,w))
            graph[v].append((u,w))
        def djikstra(node):
            heap = [(0,node)]
            dist =[float('inf')]*n;dist[node]=0
            while heap:
                dis,curr=heappop(heap)
                if dis > dist[curr]: 
                    continue
                for neg,w in graph[curr]:
                    if dist[curr]+w<dist[neg]:
                        dist[neg]=dist[curr]+w
                        heappush(heap,(dist[neg],neg))
            return dist
        sdist = djikstra(0);ddist = djikstra(n-1)
        ans = [False]*len(edges);short =sdist[n-1]
        if short==float('inf'):return ans
        for i,e in enumerate(edges):
            a,b,w=e
            if sdist[a]+w+ddist[b]==short or sdist[b] + w + ddist[a] == short:
                ans[i]=True
        return ans