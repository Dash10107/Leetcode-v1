class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        fa = list(range(n))
        rank=[0]*n
        def find(x):
            if fa[x]!=x:
                fa[x]=find(fa[x])
            return fa[x]
        def union(a,b):
            x,y = find(a),find(b)
            if x==y:return
            if rank[x]<rank[y]:
                x,y=y,x
            fa[y]=x
            if rank[x]==rank[y]:rank[x]+=1
        for a,b in allowedSwaps:
            union(a,b)
        graph = defaultdict(lambda:defaultdict(int))
        for i in range(n):
            f = find(i)
            graph[f][source[i]]+=1
        ans = 0
        for i in range(n):
            f = find(i)
            if graph[f][target[i]]>0:
                graph[f][target[i]]-=1
            else:
                ans+=1
        return ans