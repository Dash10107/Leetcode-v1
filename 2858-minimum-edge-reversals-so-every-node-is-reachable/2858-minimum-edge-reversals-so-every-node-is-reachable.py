class Solution:
    def minEdgeReversals(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append((v,0))
            graph[v].append((u,1))
        ans = [0]*n
        def dfs(node,par):
            tot=0
            for neg,cost in graph[node]:
                if neg==par:continue
                tot+=cost+dfs(neg,node)
            return tot
        def dfs2(node,par):
            for neg,cost in graph[node]:
                if neg==par:continue
                if cost==0:
                    ans[neg]= ans[node]+1
                else:
                    ans[neg]=ans[node]-1
                dfs2(neg,node)
        ans[0] = dfs(0,-1)
        dfs2(0,-1)
        return ans