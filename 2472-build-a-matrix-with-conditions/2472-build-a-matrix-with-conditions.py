class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        g1= defaultdict(list);g2=defaultdict(list)
        for a,b in rowConditions:g1[a].append(b)
        for a,b in colConditions:g2[a].append(b)
        def topos(graph):
            indeg=[0]*(k+1);topo=[]
            for u in range(1,k+1):
                for v in graph[u]:indeg[v]+=1
            q = deque();vis=set()
            for u in range(1,k+1):
                if indeg[u]==0:q.append(u)
            while q:
                u = q.popleft()
                topo.append(u)
                for v in graph[u]:
                    indeg[v]-=1
                    if indeg[v]==0:q.append(v)
            return topo if len(topo)==k else []
        rtopo = topos(g1);ctopo=topos(g2)
        if len(rtopo)==0 or len(ctopo)==0:return []
        def fill(topo):
            c = Counter()
            for u in topo:c[u]=True
            for u in range(1,k+1):
                if u not in c:topo.append(u)
        fill(rtopo);fill(ctopo)
        mat = [[0]*k for _ in range(k)]
        colInd = Counter()
        for j in range(k):colInd[ctopo[j]]=j
        for i in range(k):
            mat[i][colInd[rtopo[i]]]=rtopo[i]
        return mat