class Solution:
    def findOrder(self, n: int, prereq: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        indegree = [0]*n
        for u,v in prereq:
            adj[v].append(u)
            indegree[u]+=1
        q = deque();topo=[]
        for i in range(n):
            if indegree[i]==0:q.append(i)
        while q:
            node = q.popleft()
            topo.append(node)
            for neg in adj[node]:
                indegree[neg]-=1
                if indegree[neg]==0:q.append(neg)
        return topo if len(topo)==n else []