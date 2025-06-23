class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        g = defaultdict(list)
        indegree  = [0]*n
        if n==1:
            return [0]
        for u,v in edges:
            g[u].append(v)
            g[v].append(u)
            indegree[u]+=1
            indegree[v]+=1
        q = deque([])
        for i,ind in enumerate(indegree):
            if ind==1:q.append(i)
        while n>2 :
            s = len(q)
            n-=s
            while s:
                node = q.popleft()
                for neg in g[node]:
                    indegree[neg]-=1
                    if indegree[neg]==1:
                        q.append(neg)
                s-=1
        return list(q)