class Solution:
    def findCircleNum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        adj = defaultdict(list)
        for i in range(n):
            for j in range(n):
                if mat[i][j]==1 and i!=j:
                    adj[i].append(j)
                    adj[j].append(i)
        vis = set()
        def dfs(node):
            vis.add(node)
            for neg in adj[node]:
                if not neg in vis:dfs(neg)
        ans=0
        for i in range(n):
            if i not in vis:
                ans+=1
                dfs(i)
        return ans