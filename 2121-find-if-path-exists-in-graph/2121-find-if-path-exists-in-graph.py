class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        q = deque([source])
        vis=set()
        while q:
            node = q.popleft()
            if node==destination:return True
            vis.add(node)
            for neg in graph[node]:
                if neg not in vis:
                    q.append(neg)
        return False