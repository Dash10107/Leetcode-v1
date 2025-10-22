class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        rev = [[] for _ in range(len(graph))]
        indegree = [0]*(len(graph))
        for i in range(len(graph)):
            for u in graph[i]:
                rev[u].append(i)
                indegree[i]+=1
        q = deque()
        for i in range(len(graph)):
            if indegree[i]==0:
                q.append(i)
        topo= []
        while q:
            node = q.popleft()
            topo.append(node)
            for u in rev[node]:
                indegree[u]-=1
                if indegree[u]==0:
                    q.append(u)
        return sorted(topo)