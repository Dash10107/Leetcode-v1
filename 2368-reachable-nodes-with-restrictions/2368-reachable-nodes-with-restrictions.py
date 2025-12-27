class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        vis = [False]*n
        restrict = set(restricted)
        q = deque([0])
        while q:
            node = q.popleft()
            if node in restrict or vis[node]:
                continue
            vis[node]=True
            for v in graph[node]:
                if not vis[v] and v not in restrict:
                    q.append(v)
        return sum(1 if vis[i] else 0 for i in range(n) )