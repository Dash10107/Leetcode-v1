class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        ans = [0]*n;count = [1]*n
        gr = defaultdict(list)
        for a,b in edges:
            gr[a].append(b)
            gr[b].append(a)
    
        def dfs(node,par):
            for child in gr[node]:
                if child!=par:
                    dfs(child,node)
                    count[node]+=count[child]
                    ans[node]+=ans[child]+count[child]
        def dfs2(node,par):
            for child in gr[node]:
                if child!=par:
                    ans[child]= ans[node]-count[child]+(n-count[child])
                    dfs2(child,node)
        dfs(0,-1)
        dfs2(0,-1)
        return ans
