class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        g = defaultdict(list)
        for u,v in edges:
            g[u].append(v)
            g[v].append(u)
        def dfs(node,par):
            ans = 0
            for neg in g[node]:
                if neg==par:continue
                cost = dfs(neg,node)
                if cost>0 or hasApple[neg]:
                    ans+= cost+2
            return ans
        return dfs(0,-1)