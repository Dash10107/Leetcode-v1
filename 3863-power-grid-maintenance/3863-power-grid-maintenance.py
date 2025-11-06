class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        par = list(range(c+1))
        def find(x):
            while par[x]!=x:
                par[x]=par[par[x]]
                x=par[x]
            return par[x]
        def union(a,b):
            x,y=find(a),find(b)
            if x!=y:
                par[y]=x
        for u,v in connections:
            union(u,v)
        comps = defaultdict(list)
        for i in range(1,c+1):
            heappush(comps[find(i)],i)
        online = [1]*(c+1)
        ans = []
        for t,q in queries:
            if t==1:
                if online[q]:ans.append(q)
                else:
                    comp = comps[find(q)]
                    while comp and not online[comp[0]]:
                        heappop(comp)
                    ans.append(comp[0] if comp else -1)
            else:
                online[q]=0
        return ans

