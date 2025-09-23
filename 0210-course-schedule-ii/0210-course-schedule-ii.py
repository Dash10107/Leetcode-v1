class Solution:
    def findOrder(self, n: int, prereq: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        indegree = [0]*n
        for u,v in prereq:
            adj[v].append(u)
            indegree[u]+=1
        q = deque()
        for i in range(n):
            if indegree[i]==0:q.append(i)
        topo = []
        while q:
            node = q.popleft()
            topo.append(node)
            for u in adj[node]:
                indegree[u]-=1
                if indegree[u]==0:q.append(u)
        return topo if len(topo)==n else []