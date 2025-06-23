class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        g = defaultdict(list)
        indegree = [0]*n
        for u,v in edges:
            g[u].append(v)
            indegree[v]+=1
        ans = [set() for _ in range(n)]
        q = deque([])
        for i,ind in enumerate(indegree):
            if ind==0:q.append(i)
        while q:
            for _ in range (len(q)):
                node = q.popleft()
                for child in g[node]:
                    ans[child].add(node)
                    for anc in ans[node]:
                        ans[child].add(anc)
                    indegree[child]-=1
                    if indegree[child]==0:q.append(child)
        for i in range(n):
            ans[i]=sorted(list(ans[i]))
        return ans 