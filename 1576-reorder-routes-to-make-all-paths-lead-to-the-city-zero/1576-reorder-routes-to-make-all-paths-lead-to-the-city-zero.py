class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        def dfs(g,vis,start):
            vis[start]=True
            change =0
            for to in g[start]:
                if not vis[abs(to)]:
                    change+= dfs(g,vis,abs(to))+(1 if to>0 else 0)
            return change

        graph = defaultdict(list)
        for u,v in connections:
            graph[u].append(v)
            graph[v].append(-u)
        return dfs(graph,[False]*n,0)