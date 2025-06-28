class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]: 
        graph = defaultdict(list)
        for u,v in redEdges:
            graph[u].append((v,True))
        for u,v in blueEdges:
            graph[u].append((v,False))
        dist = [[float('inf')] * 2 for _ in range(n)]
        dist[0][0] = dist[0][1] = 0  
        heap = [(0,0,True),(0,0,False)]
        while heap:
            weight,node,red=heappop(heap)
            for neg,r in graph[node]:
                if red!=r:
                    col =  0 if r else 1
                    if weight+1<dist[neg][col]:
                        dist[neg][col]=weight+1
                        heappush(heap,(weight+1,neg,r))
        res = []
        for r,b in dist:
            t = min(r,b)
            res.append(t if t!=float('inf') else -1)
        return res