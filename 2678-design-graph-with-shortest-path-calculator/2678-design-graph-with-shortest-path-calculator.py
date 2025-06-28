class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.graph = defaultdict(list)
        self.n = n
        for u,v,w in edges:
            self.graph[u].append((v,w))

    def addEdge(self, edge: List[int]) -> None:
        u,v,w = edge
        self.graph[u].append((v,w))
        

    def shortestPath(self, start: int, end: int) -> int:
        dist = [float('inf')]*self.n
        heap = [(0,start)]
        dist[start]=0
        while heap:
            weight,node = heappop(heap)
            if node ==end:
                return weight
            for neg,w in self.graph[node]:
                if weight+w<dist[neg]:
                    dist[neg]=weight+w
                    heappush(heap,(weight+w,neg))
        return -1

# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)