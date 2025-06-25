class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        dist =  [0]*n
        for i in range(1,n):
            graph[i-1].append(i)
            dist[i]=i
        ans  = []
        def bfs(g,st,end):
            q = deque([(st,0)])
            vis = [False]*n
            vis[st]=True
            while q:
                node,lev = q.popleft()
                if dist[node]>lev:
                    dist[node]=lev
                for neg in graph[node]:
                    if not vis[neg]:
                        vis[neg]=True
                        q.append((neg,lev+1))
            return

        for u,v in queries:
            graph[u].append(v)
            bfs(graph,0,n-1)
            ans.append(dist[n-1])
        return ans