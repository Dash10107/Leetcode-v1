class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        vis = set()
        def dfs(node):
            if node==destination:return True
            vis.add(node)
            for neg  in graph[node]:
                if neg not in vis:
                    if dfs(neg):return True
            return False
        return dfs(source)